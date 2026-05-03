import numpy as np
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.linalg import eigsh
import time

def compute_topological_lifetime_sparse(H, N, k_ratio=0.3, max_k=200):
    """
    Compute τ_topo using sparse eigensolver with adaptive k.
    
    Parameters:
    -----------
    H : sparse matrix
    N : int (system size)
    k_ratio : fraction of eigenvalues to compute (0.1-0.3)
    max_k : maximum number of eigenvalues
    """
    # Adapt k based on system size
    k = min(int(N * k_ratio), max_k, N - 2)
    k = max(k, 2)  # At least 2 eigenvalues
    
    if k >= N - 1:
        k = max(N // 4, 2)
    
    print(f"    Computing {k} eigenvalues (N={N})")
    
    try:
        # Use shift-invert mode for better numerical stability
        if k < N - 1:
            E, V = eigsh(H, k=k, which='SM', maxiter=10000, tol=1e-6)
        else:
            # Fallback for very small N
            H_dense = H.toarray()
            E, V = np.linalg.eigh(H_dense)
            k = len(E)
    except Exception as e:
        print(f"    Warning: {e}")
        # Final fallback
        H_dense = H.toarray()
        E, V = np.linalg.eigh(H_dense)
        k = len(E)
    
    # Compute participation ratio for each eigenstate
    PR = np.array([1.0 / np.sum(np.abs(v)**4) for v in V.T[:k]])
    
    # Inverse participation ratio (localization)
    IPR = 1.0 / PR
    
    # Estimate gap from lowest eigenvalues
    if len(E) > 2:
        # Use the smallest positive gap (excluding spectral flattening)
        gaps = E[1:] - E[:-1]
        # Filter very small gaps (numerical noise)
        gaps = gaps[gaps > 1e-8]
        if len(gaps) > 0:
            gap = np.min(gaps)
        else:
            gap = 0
    else:
        gap = 0
    
    # Localization length estimate
    xi = np.sqrt(np.median(IPR)) if len(IPR) > 0 else 0
    
    return {
        'tau': 1.0 / (gap + 1e-10),
        'gap': gap,
        'PR_median': np.median(PR) if len(PR) > 0 else 0,
        'IPR_median': np.median(IPR) if len(IPR) > 0 else 0,
        'xi': xi,
        'k_computed': k
    }


def build_phason_hamiltonian_sparse(pts, edges, weights, ammann_lines, N, flux=0.2):
    """
    Build sparse phason-respecting Hamiltonian.
    """
    # Precompute phason coordinates
    phason = np.zeros(N)
    
    # Simplified phason from Ammann line crossings
    for line_idx, line in enumerate(ammann_lines):
        d = line.get('direction', np.array([1.0, 0.0]))
        for i, pt in enumerate(pts):
            # Perpendicular distance (using 2D cross product)
            cross = d[0] * pt[1] - d[1] * pt[0]
            sign = 1 if cross > 0 else -1
            phason[i] += sign * np.exp(-line_idx / (len(ammann_lines) + 1))
    
    # Normalize phason
    if N > 0:
        phason = phason / np.sqrt(5)
    
    # 5-fold Ammann directions
    ammann_dirs = np.array([
        [np.cos(2*np.pi*k/5), np.sin(2*np.pi*k/5)]
        for k in range(5)
    ])
    
    # Build sparse matrix
    H_lil = lil_matrix((N, N), dtype=np.complex128)
    
    for idx, (i, j) in enumerate(edges):
        w = weights[idx]
        dr = pts[j] - pts[i]
        dr_norm = dr / (np.linalg.norm(dr) + 1e-10)
        
        # Phason gradient along edge
        d_phason = phason[j] - phason[i]
        
        # Project onto nearest Ammann direction
        ammann_proj = max(abs(np.dot(dr_norm, d)) for d in ammann_dirs)
        
        # Structured phase
        phase = np.exp(1j * flux * (d_phason + 0.5 * ammann_proj * np.linalg.norm(dr)))
        
        H_lil[i, j] = w * phase
        H_lil[j, i] = np.conj(w * phase)
    
    # Convert to CSR
    H_csr = H_lil.tocsr()
    H_csr = (H_csr + H_csr.conj().T) / 2
    
    return H_csr


def detect_ammann_lines_fast(pts, edges, num_directions=5):
    """
    Fast Ammann line detection.
    """
    if len(edges) == 0:
        return [{'direction': np.array([np.cos(2*np.pi*k/5), np.sin(2*np.pi*k/5)]), 'count': 0} 
                for k in range(num_directions)]
    
    # Compute edge orientations
    orientations = []
    for i, j in edges[:min(1000, len(edges))]:
        dr = pts[j] - pts[i]
        angle = np.arctan2(dr[1], dr[0])
        orientations.append(angle)
    
    orientations = np.array(orientations)
    
    # 5 Ammann directions
    target_angles = np.array([2*np.pi*k/5 for k in range(5)])
    
    lines = []
    for k, angle in enumerate(target_angles):
        # Count edges aligned with this direction
        angle_diff = np.abs(np.sin(orientations - angle))
        count = np.sum(angle_diff < 0.3)
        lines.append({
            'direction': np.array([np.cos(angle), np.sin(angle)]),
            'count': count,
            'angle': angle
        })
    
    return lines


def run_scaling_test_sparse(N_values, flux=0.2, output_dir="/mnt/agents/output"):
    """
    Run scaling test with adaptive eigenvalue count.
    """
    results = []
    
    for N in N_values:
        print(f"\n{'='*60}")
        print(f"Running N={N}")
        print(f"{'='*60}")
        
        # Generate Penrose tiling
        start_time = time.time()
        pts = build_penrose_cut_project(N)
        print(f"  Points: {len(pts)}")
        
        if len(pts) < N:
            print(f"  Warning: Only {len(pts)} points generated (target {N})")
            pts = pts[:N] if len(pts) >= N else pts
        
        # Build graph
        edges, weights, _ = build_graph(pts, k=6)
        print(f"  Edges: {len(edges)}")
        
        # Detect Ammann lines
        ammann_lines = detect_ammann_lines_fast(pts, edges)
        print(f"  Ammann lines: {len(ammann_lines)}")
        
        # Build sparse Hamiltonian
        H = build_phason_hamiltonian_sparse(pts, edges, weights, ammann_lines, len(pts), flux)
        print(f"  Non-zero entries: {H.nnz}")
        
        # Compute topological lifetime (adaptive k)
        tau_data = compute_topological_lifetime_sparse(H, len(pts), k_ratio=0.15, max_k=150)
        print(f"  Gap: {tau_data['gap']:.6f}")
        print(f"  τ_topo: {tau_data['tau']:.2f}")
        print(f"  PR_median: {tau_data['PR_median']:.2f}")
        print(f"  ξ: {tau_data['xi']:.4f}")
        print(f"  Time: {time.time() - start_time:.1f}s")
        
        results.append({
            'N': N,
            'tau': tau_data['tau'],
            'gap': tau_data['gap'],
            'PR_median': tau_data['PR_median'],
            'xi': tau_data['xi'],
            'k_computed': tau_data['k_computed']
        })
    
    return results


def build_penrose_cut_project(N_target=300, window=2.5):
    """
    Generate Penrose tiling vertices via 5D -> 2D cut-and-project.
    Optimized for speed.
    """
    phi = (1 + np.sqrt(5)) / 2
    angles = 2 * np.pi * np.arange(5) / 5
    P = np.vstack([np.cos(angles), np.sin(angles)])
    Q = np.eye(5) - P.T @ np.linalg.pinv(P.T)
    
    pts = []
    R = int(np.ceil(N_target**(1/5))) + 2
    
    for x0 in range(-R, R):
        for x1 in range(-R, R):
            for x2 in range(-R, R):
                for x3 in range(-R, R):
                    for x4 in range(-R, R):
                        n = np.array([x0, x1, x2, x3, x4], dtype=float)
                        internal = Q @ n
                        if np.linalg.norm(internal) < window:
                            phys = P @ n
                            pts.append(phys)
                        if len(pts) >= N_target:
                            return np.array(pts)
    
    return np.array(pts)


def build_graph(pts, k=6):
    """Build k-nearest-neighbor graph."""
    from scipy.spatial import KDTree
    tree = KDTree(pts)
    dists, inds = tree.query(pts, k=min(k+1, len(pts)))
    
    edges = []
    weights = []
    edge_lookup = {}
    
    for i in range(len(pts)):
        for j in inds[i, 1:]:
            if i < j:
                d = np.linalg.norm(pts[i] - pts[j])
                w = np.exp(-d / 0.5)
                edges.append((i, j))
                weights.append(w)
                edge_lookup[(i, j)] = len(edges) - 1
    
    return edges, weights, edge_lookup


def analyze_scaling(results):
    """Analyze τ_topo scaling with N."""
    N_vals = np.array([r['N'] for r in results])
    tau_vals = np.array([r['tau'] for r in results])
    gap_vals = np.array([r['gap'] for r in results])
    
    print(f"\n{'='*60}")
    print("SCALING ANALYSIS")
    print(f"{'='*60}")
    print(f"\n{'N':>8} {'τ_topo':>12} {'Gap':>12} {'PR_median':>12} {'ξ':>10}")
    print("-"*60)
    for r in results:
        print(f"{r['N']:>8} {r['tau']:>12.2f} {r['gap']:>12.6f} {r['PR_median']:>12.2f} {r['xi']:>10.4f}")
    
    # Find peaks
    from scipy.signal import find_peaks
    peaks, _ = find_peaks(tau_vals, height=np.median(tau_vals)*1.5)
    
    if len(peaks) >= 2:
        N_peak = N_vals[peaks]
        tau_peak = tau_vals[peaks]
        
        logN = np.log(N_peak)
        logtau = np.log(tau_peak)
        
        from scipy.stats import linregress
        slope, intercept, r_value, p_value, std_err = linregress(logN, logtau)
        
        print(f"\nPEAK SCALING (τ_peak ~ N^α):")
        print(f"  α = {slope:.4f} ± {std_err:.4f}")
        print(f"  R² = {r_value**2:.4f}")
        print(f"  Target φ-scaling: {np.log((1+np.sqrt(5))/2):.4f}")
        
        target = np.log((1+np.sqrt(5))/2)
        if abs(slope - target) < 0.15:
            print(f"\n  ✓ MATCH: Singular-continuous spectrum")
        elif slope < target:
            print(f"\n  ⚠ Below target — need larger N")
        else:
            print(f"\n  ⚠ Above target — check methodology")
    else:
        print(f"\n  Insufficient peaks for scaling analysis")
        print(f"  Found {len(peaks)} peaks (need ≥2)")
    
    return results


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    # Fibonacci sequence for Penrose tiling
    # Start smaller to verify the code works
    N_values = [100, 200, 300, 500, 800]  # First run these
    
    print("="*70)
    print("SPARSE EIGENSOLVER SCALING TEST")
    print(f"N values: {N_values}")
    print("="*70)
    
    results = run_scaling_test_sparse(N_values)
    analyze_scaling(results)
    
    # Save results
    import pickle
    with open(f"{output_dir}/sparse_scaling_results.pkl", 'wb') as f:
        pickle.dump(results, f)
    print(f"\nResults saved to: {output_dir}/sparse_scaling_results.pkl")
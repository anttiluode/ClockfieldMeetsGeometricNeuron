"""
overlap_dirac_index.py
======================
Closing the Atiyah-Singer bridge for the Clockfield background.
Constructs a massless 2D Wilson-Dirac operator, builds the Ginsparg-Wilson 
overlap operator, and calculates the topological index via the trace formula.

Test cases:
1. Pure Gauge Vortex (Torus) - Should yield Index = 0 (The March Artifact)
2. True Unit Flux (Q=1)      - Should yield Index = +1

Do not hype. Do not lie. Just show.
"""

import numpy as np

def run_overlap_index_test():
    N = 16  # Lattice size (N x N)
    dim = 2 * N**2
    m0 = 1.0  # Domain wall mass / negative mass shift

    # 2D Euclidean Gamma Matrices (Pauli matrices)
    gamma1 = np.array([[0, 1], [1, 0]], dtype=complex)
    gamma2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    gamma5 = np.array([[1, 0], [0, -1]], dtype=complex)  # sigma_3

    def get_index(U1, U2, label):
        # 1. Verify the total plaquette flux (Topological Charge Q)
        total_flux = 0.0
        for x in range(N):
            for y in range(N):
                # P(x,y) = U_1(x,y) * U_2(x+1,y) * U_1^*(x,y+1) * U_2^*(x,y)
                p = (U1[x, y] * U2[(x+1)%N, y] * np.conj(U1[x, (y+1)%N]) * np.conj(U2[x, y]))
                total_flux += np.angle(p)
        
        Q_measured = total_flux / (2 * np.pi)

        # 2. Construct the Wilson-Dirac Operator D_W
        D_W = np.zeros((dim, dim), dtype=complex)
        
        def idx(x, y, s):
            return (x * N + y) * 2 + s

        for x in range(N):
            for y in range(N):
                for s in range(2):
                    i = idx(x, y, s)
                    D_W[i, i] = 2.0  # Diagonal Wilson term (2r, r=1)
                    
                    # +x shift
                    x_up = (x+1) % N
                    u1 = U1[x, y]
                    for s2 in range(2):
                        D_W[i, idx(x_up, y, s2)] += 0.5 * u1 * (gamma1[s, s2] - 1.0 * (s==s2))
                        
                    # -x shift
                    x_dn = (x-1) % N
                    u1_dn = np.conj(U1[x_dn, y])
                    for s2 in range(2):
                        D_W[i, idx(x_dn, y, s2)] += 0.5 * u1_dn * (-gamma1[s, s2] - 1.0 * (s==s2))

                    # +y shift
                    y_up = (y+1) % N
                    u2 = U2[x, y]
                    for s2 in range(2):
                        D_W[i, idx(x, y_up, s2)] += 0.5 * u2 * (gamma2[s, s2] - 1.0 * (s==s2))
                        
                    # -y shift
                    y_dn = (y-1) % N
                    u2_dn = np.conj(U2[x, y_dn])
                    for s2 in range(2):
                        D_W[i, idx(x, y_dn, s2)] += 0.5 * u2_dn * (-gamma2[s, s2] - 1.0 * (s==s2))

        # 3. Construct Hermitian Wilson operator: H_W = gamma5 * (D_W - m0)
        G5_block = np.kron(np.eye(N**2), gamma5)
        H_W = G5_block @ (D_W - m0 * np.eye(dim))

        # 4. Diagonalize H_W to compute sign(H_W)
        evals, evecs = np.linalg.eigh(H_W)
        
        # Spectral gap check (if minimum eval is ~0, topology is ill-defined)
        min_gap = np.min(np.abs(evals))
        
        sign_evals = np.sign(evals)
        sign_H_W = evecs @ np.diag(sign_evals) @ evecs.conj().T

        # 5. The Overlap Index Theorem: Index = -1/2 Tr(gamma5 * sign(H_W))
        dirac_index = 0.5 * np.trace(sign_H_W)

        print(f"--- {label} ---")
        print(f"  Plaquette Charge (Q) : {np.round(Q_measured, 4)}")
        print(f"  Dirac Operator Index : {np.round(np.real(dirac_index), 4)}")
        print(f"  H_W Spectral Gap     : {np.round(min_gap, 4)}\n")

    print("="*60)
    print(" GINSPARG-WILSON DIRAC OPERATOR INDEX TEST")
    print("="*60)

    # ---------------------------------------------------------
    # TEST 1: Pure Gauge Vortex on a Torus (The March Artifact)
    # ---------------------------------------------------------
    # A single vortex without properly regulating the boundaries or core.
    U1_pg = np.ones((N, N), dtype=complex)
    U2_pg = np.ones((N, N), dtype=complex)
    x0, y0 = N/2, N/2
    for x in range(N):
        for y in range(N):
            theta = np.arctan2(y - y0, x - x0)
            theta_x = np.arctan2(y - y0, ((x+1)%N) - x0)
            theta_y = np.arctan2(((y+1)%N) - y0, x - x0)
            U1_pg[x,y] = np.exp(1j * (theta_x - theta))
            U2_pg[x,y] = np.exp(1j * (theta_y - theta))
            
    get_index(U1_pg, U2_pg, "Test 1: Pure Gauge Vortex (Periodic Torus)")

    # ---------------------------------------------------------
    # TEST 2: True Unit Flux (Q=1) Background
    # ---------------------------------------------------------
    # Flux is uniformly distributed to explicitly prevent periodic cancellation.
    Q = 1.0
    U1_true = np.ones((N, N), dtype=complex)
    U2_true = np.ones((N, N), dtype=complex)
    for x in range(N):
        for y in range(N):
            # Landau gauge A_1 = -2pi*Q*y / N^2
            U1_true[x, y] = np.exp(1j * (-2 * np.pi * Q * y / (N**2)))
            # Boundary twist to enforce periodicity in y
            if y == N - 1:
                U2_true[x, y] = np.exp(1j * 2 * np.pi * Q * x / N)

    get_index(U1_true, U2_true, "Test 2: Genuine Unit Flux (Q=1)")

if __name__ == "__main__":
    run_overlap_index_test()
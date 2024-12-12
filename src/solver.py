import numpy as np
import scipy as sp


class MAP:
    def __init__(self, max_iteration, tolerance, verbose=False):
        """
        Method of Alternating Projections.

        Arguments

        - `max_iteration` - Maximum number of iterations.
        - `tolerance`     - Convergence tolerance for the error.
        - `verbose`       - Verbosity.
        """
        self.max_iter = max_iteration
        self.tol = tolerance
        self.verbose = verbose

    def solve(self, mat_A, vec_c, initial=None):
        """
        Solve the problem using the Method of Alternating Projections.

        Arguments

        - `mat_A`   - Matrix $A$ of size (m, n).
        - `vec_c`   - Vector $c$ of size (m,).
        - `initial` - Initial guess vector of size (2n,).

        Returns

        - `vec_x` - Solution vector of size (n,).
        """
        n = mat_A.shape[1]
        mat_I = np.eye(n)  # -mat_B
        mat_T = np.hstack([mat_A - mat_I, -mat_A - mat_I])

        # pre-compute cholesky factor for efficiency (page. 29)
        chol_factor, chol_bool = sp.linalg.cho_factor(2 * (mat_A @ mat_A.T + mat_I))
        cbar = np.sqrt(2) * vec_c

        # initialization
        if initial is None:
            vec_w = mat_T.T @ sp.linalg.cho_solve((chol_factor, chol_bool), cbar)
        else:
            assert (
                len(initial) == 2 * n
            ), "dimension of initial guess must be {}".format(2 * n)
            vec_w = initial

        for i in range(self.max_iter):
            # Projection onto C2 (Proposition 2.2)
            vec_u = vec_w[:n]  # first-half of `vec_w`
            vec_v = vec_w[n:]  # second-half of `vec_w`
            mask = (vec_u < 0) & (vec_v < 0)  # both negative
            vec_u = np.where(mask, 0, np.where(vec_u >= vec_v, vec_u, 0))
            vec_v = np.where(mask, 0, np.where(vec_v >= vec_u, vec_v, 0))
            pc2_w = np.hstack([vec_u, vec_v])

            # Projection onto C1 (Proposition 2.1)
            # solve `vec_z` by Equation (4.1)
            vec_z = sp.linalg.cho_solve((chol_factor, chol_bool), mat_T @ pc2_w - cbar)
            # compute `mat_T.T @ vec_z` by `vec_p` for computational efficiency (page. 29)
            vec_p = mat_A.T @ vec_z
            pc1_w = pc2_w - np.hstack([vec_p - vec_z, -vec_p - vec_z])

            vec_x = (pc1_w[:n] - pc1_w[n:]) / np.sqrt(2)

            err = np.linalg.norm(mat_A @ vec_x - np.abs(vec_x) - vec_c)
            if err < self.tol:
                if self.verbose:
                    print("iterations: {}".format(i + 1))
                    print("error: {:.5f}".format(err), end="\n\n")
                break

            vec_w = pc1_w

        return vec_x

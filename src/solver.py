# Copyright 2024 Bang-Shien Chen.
# All rights reserved. See LICENSE for the license information.

import numpy as np
import scipy as sp


class MAP:
    def __init__(
        self, max_iteration, tolerance, relative_tolerance=1e-6, verbose=False
    ):
        """
        Method of Alternating Projections.

        Arguments

        - `max_iteration`      - Maximum number of iterations.
        - `tolerance`          - Absolute tolerance for the error.
        - `relative_tolerance` - Relative tolerance for early stop.
        - `verbose`            - Verbosity.
        """
        self.max_iter = max_iteration
        self.tol = tolerance
        self.rel_tol = relative_tolerance
        self.verbose = verbose

    def solve(self, mat_A, mat_B, vec_c, initial=None):
        """
        Solve an Absolute Value Equation

            $$ Ax + B|x| = c $$

        using the Method of Alternating Projections.

        Arguments

        - `mat_A`   - Matrix $A$ of size (m, n).
        - `mat_B`   - Matrix $B$ of size (m, n).
        - `vec_c`   - Vector $c$ of size (m,).
        - `initial` - Initial guess vector of size (2n,).

        Returns

        - `vec_x` - Solution vector of size (n,).
        """
        m, n = mat_A.shape
        mat_T = np.hstack([mat_A + mat_B, -mat_A + mat_B])
        cbar = np.sqrt(2) * vec_c

        # check full rank case by Lemma 2.8
        case_full_rank = False
        if m == n and np.allclose(mat_B, -np.eye(3)):
            case_full_rank = True

        # pre-compute cholesky factor for efficiency (page. 29)
        chol_factor, chol_bool = sp.linalg.cho_factor(
            2 * (mat_A @ mat_A.T + mat_B @ mat_B.T)
        )

        # initialization
        if initial is None:
            vec_w = mat_T.T @ sp.linalg.cho_solve((chol_factor, chol_bool), cbar)
        else:
            assert (
                len(initial) == 2 * n
            ), "dimension of initial guess must be {}".format(2 * n)
            vec_w = initial

        prev_cost = 1e10
        for i in range(self.max_iter):
            # projection onto C2 (Proposition 2.2)
            vec_u = vec_w[:n]  # first-half of `vec_w`
            vec_v = vec_w[n:]  # second-half of `vec_w`
            mask = (vec_u < 0) & (vec_v < 0)  # both negative
            vec_u = np.where(mask, 0, np.where(vec_u >= vec_v, vec_u, 0))
            vec_v = np.where(mask, 0, np.where(vec_v >= vec_u, vec_v, 0))
            pc2_w = np.hstack([vec_u, vec_v])

            # projection onto C1 (Proposition 2.1)
            # solve `vec_z` by Equation (4.1)
            vec_z = sp.linalg.cho_solve((chol_factor, chol_bool), mat_T @ pc2_w - cbar)

            if case_full_rank:
                # compute `mat_T.T @ vec_z` by `vec_p` for efficiency (page. 29)
                vec_p = mat_A.T @ vec_z
                pc1_w = pc2_w - np.hstack([vec_p - vec_z, -vec_p - vec_z])
            else:
                pc1_w = pc2_w - mat_T.T @ vec_z 

            vec_x = (pc1_w[:n] - pc1_w[n:]) / np.sqrt(2)

            # stopping criteria
            cost = np.linalg.norm(mat_A @ vec_x + mat_B @ np.abs(vec_x) - vec_c)
            if (
                cost < self.tol
                or abs(cost - prev_cost) / max(prev_cost, 1e-7) < self.rel_tol
            ):
                break

            vec_w = pc1_w
            prev_cost = cost

        if self.verbose:
            print("iterations: {}".format(i + 1))
            print("error: {:.5f}".format(cost), end="\n\n")

        return vec_x

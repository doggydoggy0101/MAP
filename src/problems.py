# Copyright 2024 Bang-Shien Chen.
# All rights reserved. See LICENSE for the license information.

import numpy as np
import scipy as sp


class Problems:
    def __init__(self, m, n, random_seed=42):
        """
        Generate an Absolute Value Equation problem

            $$ Ax + B|x| = c $$

        with matrix $A$ of size (m, n), matrix $B$ of size (m, n),
        vector $c$ of size m, and ground truth solution of size n.

        Arguments

        - `m`           - Problem size parameter.
        - `n`           - Problem size parameter.
        - `random_seed` - Random seed for random generator.
        """
        self.m = m
        self.n = n
        self.rng = np.random.default_rng(random_seed)

    def problem1(self, alpha=0):
        """
        Problem 1 (Example 4.1)

        Arguments

        - `alpha` - Problem parameter in {0, 1, 2, 3}.

        Returns

        - `mat_A` - Matrix $A$ in AVE.
        - `mat_B` - Matrix $B$ in AVE.
        - `vec_c` - Vector $c$ in AVE.
        - `sol_x` - Ground truth solution.
        """
        mat_A = -10 + 20 * self.rng.random(size=(self.m, self.n))
        mat_A /= min(sp.linalg.svdvals(mat_A)) * self.rng.random()
        mat_B = -np.eye(self.m, self.n)

        sol_x = -1 + 2 * self.rng.random(size=self.n)
        if alpha:
            sol_x *= 10 ** (alpha * self.rng.random(size=self.n))

        vec_c = mat_A @ sol_x + mat_B @ abs(sol_x)

        return mat_A, mat_B, vec_c, sol_x

    def problem2(self):
        """
        Problem 2 (Example 4.2)

        Returns

        - `mat_A` - Matrix $A$ in AVE.
        - `mat_B` - Matrix $B$ in AVE.
        - `vec_c` - Vector $c$ in AVE.
        - `sol_x` - Ground truth solution.
        """
        assert self.m == self.n, "m and n must have the same size for this problem"
        vec_A = self.rng.normal(size=self.n)[None, :]
        mat_A = vec_A * vec_A.T
        mat_B = -np.eye(self.n)

        sol_x = self.rng.normal(size=self.n)

        vec_c = mat_A @ sol_x + mat_B @ abs(sol_x)

        return mat_A, mat_B, vec_c, sol_x

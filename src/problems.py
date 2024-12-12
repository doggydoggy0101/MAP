import numpy as np
import scipy as sp


class Problems:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def problem1(self, alpha=0):
        """
        Problem 1 (Example 4.1)

        Arguments

        - `alpha` - Problem parameter in {0, 1, 2, 3}.

        Returns

        - `mat_A` - Matrix $A$ for AVE.
        - `mat_B` - Matrix $B$ for AVE.
        - `vec_c` - Vector $c$ for AVE.
        - `sol_x` - Ground truth solution.
        """
        mat_A = -10 + 20 * np.random.rand(self.m, self.n)
        mat_A /= min(sp.linalg.svdvals(mat_A)) * np.random.rand()
        mat_B = -np.eye(self.m, self.n)

        sol_x = -1 + 2 * np.random.rand(self.n)
        if alpha:
            sol_x *= 10 ** (alpha * np.random.rand(self.n))

        vec_c = mat_A @ sol_x + mat_B @ abs(sol_x)

        return mat_A, mat_B, vec_c, sol_x

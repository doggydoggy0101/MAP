# Copyright 2024 Bang-Shien Chen.
# All rights reserved. See LICENSE for the license information.

from src.problems import Problems
from src.solver import MAP

m = 15
n = 10

MAX_ITER = 1000
TOL = 1e-6
REL_TOL = 1e-6  # early stop
VERBOSE = True

prob = Problems(m, n)  # change random seed here
mat_A, mat_B, vec_c, gtruth = prob.problem1()  # change problem index here
print("Ground truth solution:\n", gtruth, end="\n\n")

model = MAP(MAX_ITER, TOL, REL_TOL, VERBOSE)
sol = model.solve(mat_A, mat_B, vec_c)
print("MAP solution:\n", sol, end="\n\n")

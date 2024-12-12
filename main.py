from src.problems import Problems
from src.solver import MAP

m = 10
n = 10

MAX_ITER = 1000
TOL = 1e-6
VERBOSE = True

prob = Problems(m, n)
mat_A, mat_B, vec_c, gtruth = prob.problem1()  # change problem index here
print("Ground truth solution:\n", gtruth, end="\n\n")

model = MAP(MAX_ITER, TOL, VERBOSE)
sol = model.solve(mat_A, vec_c)
print("MAP solution:\n", sol, end="\n\n")

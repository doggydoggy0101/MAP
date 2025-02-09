# Copyright 2025 Bang-Shien Chen.
# All rights reserved. See LICENSE for the license information.

try:
    import map_python
except ImportError:
    print("Make sure project was built with python binding.")
    exit(1)


def main():
    max_iter = 1000
    tol = 1e-6
    rel_tol = 1e-6

    m = 10
    n = 10

    problem = map_python.Problem()
    mat_A, mat_B, vec_c, gtruth = problem.generate_problem1(m, n)

    solver = map_python.Solver(
        max_iteration=max_iter, tolerance=tol, relative_tolerance=rel_tol, verbose=True
    )
    sol = solver.solve(mat_A, mat_B, vec_c)

    print("Ground truth:")
    print(gtruth, end="\n\n")

    print("MAP solution:")
    print(sol, end="\n\n")


if __name__ == "__main__":
    main()

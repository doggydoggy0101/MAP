/**
 * Copyright 2025 Bang-Shien Chen.
 * All rights reserved. See LICENSE for the license information.
 */

#include <iostream>

#include "problem.h"
#include "solver.h"

int main() {
  size_t max_iter = 1000;
  double tol = 1e-6;
  double rel_tol = 1e-6;
  bool verbose = true;

  int m = 10;
  int n = 10;

  MAP::Problem problem;
  auto [mat_A, mat_B, vec_c, gtruth] = problem.generate_problem1(m, n);

  MAP::Solver solver(max_iter, tol, rel_tol, verbose);
  Eigen::VectorXd sol = solver.solve(mat_A, mat_B, vec_c);

  std::cout << "Ground Truth:" << "\n" << gtruth.transpose() << "\n\n";
  std::cout << "MAP solution:" << "\n" << sol.transpose() << "\n\n";

  return 0;
}
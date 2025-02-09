/**
 * Copyright 2025 Bang-Shien Chen.
 * All rights reserved. See LICENSE for the license information.
 */
#include "problem.h"

namespace MAP {

// Constructor: Initializes RNG with a default seed (42) or a user-provided seed
Problem::Problem(int seed) : rng(seed) {}

std::tuple<Eigen::MatrixXd, Eigen::MatrixXd, Eigen::VectorXd, Eigen::VectorXd> Problem::generate_problem1(
    int m, int n, int alpha) const {
  Eigen::MatrixXd mat_A = Eigen::MatrixXd::NullaryExpr(m, n, [&] { return uniform_dist(rng); });

  // Normalize A using eigenvalues instead of full SVD
  Eigen::SelfAdjointEigenSolver<Eigen::MatrixXd> eig_solver(mat_A.transpose() * mat_A);
  mat_A /= std::sqrt(eig_solver.eigenvalues().minCoeff());

  Eigen::MatrixXd mat_B = -Eigen::MatrixXd::Identity(m, n);

  Eigen::VectorXd sol_x = Eigen::VectorXd::NullaryExpr(n, [&] { return uniform_dist(rng) / 10.0; });

  if (alpha > 0) {
    sol_x.array() *= std::exp2(alpha * uniform_dist(rng));
  }

  Eigen::VectorXd vec_c = mat_A * sol_x + mat_B * sol_x.cwiseAbs();

  return {mat_A, mat_B, vec_c, sol_x};
}

std::tuple<Eigen::MatrixXd, Eigen::MatrixXd, Eigen::VectorXd, Eigen::VectorXd> Problem::generate_problem2(int n) const {
  Eigen::VectorXd vec_A = Eigen::VectorXd::NullaryExpr(n, [&] { return normal_dist(rng); });

  Eigen::MatrixXd mat_A = vec_A * vec_A.transpose();
  Eigen::MatrixXd mat_B = -Eigen::MatrixXd::Identity(n, n);

  Eigen::VectorXd sol_x = Eigen::VectorXd::NullaryExpr(n, [&] { return normal_dist(rng); });

  Eigen::VectorXd vec_c = mat_A * sol_x + mat_B * sol_x.cwiseAbs();

  return {mat_A, mat_B, vec_c, sol_x};
}

}  // namespace MAP
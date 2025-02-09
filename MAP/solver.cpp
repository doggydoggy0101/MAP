/**
 * Copyright 2025 Bang-Shien Chen.
 * All rights reserved. See LICENSE for the license information.
 */
#include "solver.h"

namespace MAP {

Solver::Solver(size_t max_iteration, double tolerance, double relative_tolerance, bool verbose) {
  max_iteration_ = max_iteration;
  tolerance_ = tolerance;
  relative_tolerance_ = relative_tolerance;
  verbose_ = verbose;
}

Eigen::VectorXd Solver::solve(const Eigen::MatrixXd& mat_A, const Eigen::MatrixXd& mat_B, const Eigen::VectorXd& vec_c,
                              std::optional<Eigen::VectorXd> initial) {
  int m = mat_A.rows();
  int n = mat_A.cols();

  Eigen::VectorXd vec_x;
  Eigen::VectorXd vec_w;
  Eigen::VectorXd vec_u;
  Eigen::VectorXd vec_v;
  Eigen::VectorXd vec_z;
  Eigen::VectorXd vec_p;
  Eigen::VectorXd pc1_w;
  Eigen::VectorXd pc2_w(2 * n);
  Eigen::Array<bool, Eigen::Dynamic, 1> mask;

  // compute matrix T
  Eigen::MatrixXd mat_T(m, 2 * n);
  mat_T << mat_A + mat_B, -mat_A + mat_B;
  Eigen::VectorXd cbar = std::sqrt(2.0) * vec_c;

  // check full-rank case (Lemma 2.8)
  bool case_full_rank = (m == n) && mat_B.isApprox(-Eigen::MatrixXd::Identity(n, n));

  // pre-compute Cholesky factor (page 29)
  Eigen::LLT<Eigen::MatrixXd> chol_factor(2 * (mat_A * mat_A.transpose() + mat_B * mat_B.transpose()));

  // initialization
  if (!initial.has_value()) {
    vec_w = mat_T.transpose() * chol_factor.solve(cbar);
  } else {
    if (initial->size() != 2 * n) {
      throw std::invalid_argument("Dimension of initial guess must be " + std::to_string(2 * n));
    }
    vec_w = initial.value();
  }

  double prev_cost = 1e10;
  for (size_t i = 0; i < max_iteration_; i++) {
    // Projection onto C2 (Proposition 2.2)
    Eigen::Map<Eigen::VectorXd> vec_u(vec_w.data(), n);
    Eigen::Map<Eigen::VectorXd> vec_v(vec_w.data() + n, n);
    // mask for elements where both vec_u and vec_v are negative
    Eigen::Array<bool, Eigen::Dynamic, 1> mask = (vec_u.array() < 0) && (vec_v.array() < 0);
    vec_u.array() = mask.select(0.0, (vec_u.array() >= vec_v.array()).select(vec_u.array(), 0.0));
    vec_v.array() = mask.select(0.0, (vec_v.array() >= vec_u.array()).select(vec_v.array(), 0.0));
    pc2_w << vec_u, vec_v;

    // project onto C1 (Proposition 2.1)
    vec_z = chol_factor.solve(mat_T * pc2_w - cbar);

    if (case_full_rank) {
      vec_p = mat_A.transpose() * vec_z;
      pc1_w = pc2_w - (Eigen::VectorXd(n * 2) << vec_p - vec_z, -vec_p - vec_z).finished();
    } else {
      pc1_w = pc2_w - mat_T.transpose() * vec_z;
    }

    vec_x = (pc1_w.head(n) - pc1_w.tail(n)) / std::sqrt(2.0);

    // stopping criterion
    double cost = (mat_A * vec_x + mat_B * vec_x.cwiseAbs() - vec_c).norm();
    if (cost < tolerance_ || std::abs(cost - prev_cost) / std::max(prev_cost, 1e-7) < relative_tolerance_) {
      if (verbose_) {
        std::cout << "Iterations: " << i + 1 << "\n";
        std::cout << "Error: " << cost << "\n\n";
      }
      break;
    }

    vec_w = pc1_w;
    prev_cost = cost;
  }

  return vec_x;
}

}  // namespace MAP
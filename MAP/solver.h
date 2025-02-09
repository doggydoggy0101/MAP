/**
 * Copyright 2025 Bang-Shien Chen.
 * All rights reserved. See LICENSE for the license information.
 */
#pragma once

#include <Eigen/Dense>
#include <algorithm>
#include <iostream>
#include <optional>

namespace MAP {

class Solver {
 public:
  /**
   * @brief MAP solver.
   * @param max_iteration Maximum number of iterations.
   * @param tolerance Tolerance for the absolute error.
   * @param relative_tolerance Tolerance for the relative error.
   * @param verbose Print result.
   */
  Solver(size_t max_iteration, double tolerance, double relative_tolerance, bool verbose);

  /**
   * @brief Solve the Absolute Value Equation $Ax + B|x| = c$.
   * @param mat_A Matrix A.
   * @param mat_B Matrix B.
   * @param vec_c Vector c.
   * @param initial Initial guess.
   * @return Solution x.
   */
  Eigen::VectorXd solve(const Eigen::MatrixXd& mat_A, const Eigen::MatrixXd& mat_B, const Eigen::VectorXd& vec_c,
                        std::optional<Eigen::VectorXd> initial = std::nullopt);

 private:
  size_t max_iteration_;
  double tolerance_;
  double relative_tolerance_;
  bool verbose_;
};

}  // namespace MAP
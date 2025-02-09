/**
 * Copyright 2025 Bang-Shien Chen.
 * All rights reserved. See LICENSE for the license information.
 */
#pragma once

#include <Eigen/Dense>
#include <cmath>
#include <random>
#include <tuple>

namespace MAP {

/**
 * @brief Generate an Absolute Value Equation problem
 * @details $Ax + B|x| = c$.
 * @return Tuple of (A, B, c, x) where x is the ground truth.
 */
class Problem {
 public:
  explicit Problem(int seed = 42);  // default random seed

  /// @brief Example 4.1
  std::tuple<Eigen::MatrixXd, Eigen::MatrixXd, Eigen::VectorXd, Eigen::VectorXd> generate_problem1(int m, int n,
                                                                                                   int alpha = 0) const;

  /// @brief Example 4.2
  std::tuple<Eigen::MatrixXd, Eigen::MatrixXd, Eigen::VectorXd, Eigen::VectorXd> generate_problem2(int n) const;

 private:
  mutable std::mt19937 rng;
  mutable std::uniform_real_distribution<double> uniform_dist{-10.0, 10.0};
  mutable std::normal_distribution<double> normal_dist{0.0, 1.0};
};

extern const Problem problem;

}  // namespace MAP
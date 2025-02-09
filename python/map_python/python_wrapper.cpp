/**
 * Copyright 2025 Bang-Shien Chen.
 * All rights reserved. See LICENSE for the license information.
 */
#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "problem.h"
#include "solver.h"

namespace py = pybind11;

PYBIND11_MODULE(map_python, module) {
  module.doc() = "Python bindings for the MAP library (Alternating Projection Solver)";

  // Bind Solver class
  py::class_<MAP::Solver>(module, "Solver")
      .def(py::init<size_t, double, double, bool>(), py::arg("max_iteration") = 1000, py::arg("tolerance") = 1e-6,
           py::arg("relative_tolerance") = 1e-6, py::arg("verbose") = false)
      .def("solve", &MAP::Solver::solve, py::arg("mat_A"), py::arg("mat_B"), py::arg("vec_c"),
           py::arg("initial") = std::nullopt);

  py::class_<MAP::Problem>(module, "Problem")
      .def(py::init<int>(), py::arg("seed") = 42)
      .def("generate_problem1", &MAP::Problem::generate_problem1, py::arg("m"), py::arg("n"), py::arg("alpha") = 0)
      .def("generate_problem2", &MAP::Problem::generate_problem2, py::arg("n"));
}
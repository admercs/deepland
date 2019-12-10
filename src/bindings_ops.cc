#include <pybind11/pybind11.h>
#include <pybind11/numpy.h> // required for vectorize()

#include "ops.h"

namespace py = pybind11;


PYBIND11_MODULE(ops, m)
{
  // Attributes
  m.doc() = "pybind11 ops plugin"; // optional module docstring
  #ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
  #else
    m.attr("__version__") = "dev";
  #endif
  // Methods
  m.def("add", &add, "A function that adds two numbers",
    py::arg("i"), py::arg("j"));
  m.def("subtract", &subtract, "A function that subtracts one number from another",
    py::arg("i"), py::arg("j"));
  m.def("square", py::vectorize(square), "A vectorized square function.",
    py::arg("x"));
}

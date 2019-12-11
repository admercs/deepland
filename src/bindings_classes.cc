//#include <pybind11/numpy.h>  // required for vectorize()
#include <pybind11/pybind11.h>

#include "classes.h"

namespace py = pybind11;

PYBIND11_MODULE(classes, m) {
  // Attributes
  m.doc() = "pybind11 classes plugin";  // optional module docstring
#ifdef VERSION_INFO
  m.attr("__version__") = VERSION_INFO;
#else
  m.attr("__version__") = "dev";
#endif
  // Classes
  py::class_<First>(m, "First")
      .def(py::init<const double &>())
      .def("get_number", &First::get_number, "getter method");
  py::class_<Second>(m, "Second")
      .def(py::init<const double &>())
      .def("set_id", &Second::set_id, "setter method", py::arg("value"))
      .def("get_id", &Second::get_id, "getter method")
      .def("get_number", &Second::get_number, "getter method");
  // Methods
  // m.def("method1", &method1, "A function", py::arg("i"), py::arg("j"));
  // m.def("method2", &method2, "A function", py::arg("i"), py::arg("j"));
}

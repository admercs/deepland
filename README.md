# deepland

[![DOI](https://zenodo.org/badge/227004053.svg)](https://zenodo.org/badge/latestdoi/227004053) [![Build Status](https://travis-ci.org/adam-erickson/deepland.svg?branch=master)](https://travis-ci.org/adam-erickson/deepland)

AGU Fall 2019: [IN43A-02: A software framework for rapid prototyping of artificial intelligence in Earth system models](https://agu.confex.com/agu/fm19/meetingapp.cgi/Paper/634946)

> Machine or deep learning represents a promising new way to represent processes in Earth system models. These models are fundamentally data-driven or pattern-based, whereby models are learned from data. This fills a critical gap in our current modeling abilities given the absence of process understanding to produce mechanistic or physical models. While machine/deep learning practitioners commonly use Python frameworks such as Scikit-Learn, TensorFlow, and PyTorch, component models of Earth systems are commonly implemented in low-level FORTRAN and may move toward C++ for its numerous industry-standard libraries. This divide between user-friendly high-level languages and high-performance low-level languages is known as the two-language problem. We address this problem by proposing the generation of a Python interface to C++ code using CMake and pybind11. This makes high-performance C++ classes and methods accessible to Python deep learning frameworks, allowing rapid prototyping of machine/deep learning process models.

<img align="center" src="fcn32.png" alt="FCN-32">

## What it is

A simple demonstration project wrapping modern C++ with Python using pybind11 (C++/Python), CMake (C/C++), setuptools (Python), GoogleTest (C++), and unittest (Python). Included are Python tools for machine and deep learning, Google Earth Engine, and fetching popular datasets. For users of the [Conan](https://conan.io/) package manager, affectionately known as *Barbarians*, we have included the requisite `conanfile.txt` file.

## How it works

CMake provides cross-platform compilation of C++ projects with a variety of compilers (e.g., gcc, clang, Apple clang, and MSVC). Building and linking the pybind11 and GoogleTest headers is included in our `CMakeLists.txt` build file. The file is run by the `setup.py` file, which uses `setuptools` to specify the Python build process. Compiling C++ code, linking it to Python, and running C++ and Python tests are accomplished with a single command:

`python setup.py test`

While C++ tests are specified using GoogleTest, the `unittest` library is used for Python tests. Additionally, Python code in `setup.py` moves the compiled C++ test binary to the `bin/` folder and automatically runs the C++ and Python tests. Separate C++ and Python tests are run to isolate errors between function implementations.

## Why pybind11

Wrapping modern C++ in Python provides high-level and high-performance code, a sort of *have-your-cake-and-eat-it* for programmers concerned with performance. If your codebase is primarily C rather than C++, similar functionality may be achieved using `Cython` rather than `pybind11`. Languages such as Julia and Python's Numba address the so-called 'two-lanuage problem' using the LLVM compiler infrastructure.

## Caveats

A fast Python interface comes at the cost of increased complexity and duplication, which `pybind11` minimizes compared to other approaches. Ultimately, `pybind11` interface addresses the two-language problem by adding a third language with its own syntax within C++. Testing frameworks such as GoogleTest add yet more domain-specific C++ syntax. Yet, such tools are indespensible for modern C++ programming. While CMake also adds complexity, it enables simplified cross-platform support.

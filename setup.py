import os
import re
import sys
import sysconfig
import platform
import subprocess

from distutils.version import LooseVersion
from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
from shutil import copyfile, copymode

from deepland import __version__


LICENSE = "Apache Software License (https://www.apache.org/licenses/LICENSE-2.0)"


class CMakeExtension(Extension):
    """CMake extension class."""

    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    """CMake build class."""

    def run(self):
        """Run the build process for each extension."""

        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError(
                "CMake must be installed to build the following extensions: " +
                ", ".join(e.name for e in self.extensions))

        if platform.system() == "Windows":
            cmake_version = LooseVersion(re.search(r'version\s*([\d.]+)',
                                         out.decode()).group(1))
            if cmake_version < '3.1.0':
                raise RuntimeError("CMake >= 3.1.0 is required on Windows")

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        """Build an extension."""

        extdir = os.path.abspath(
            os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
                      '-DPYTHON_EXECUTABLE=' + sys.executable]

        cfg = 'Debug' if self.debug else 'Release'
        build_args = ['--config', cfg]

        if platform.system() == "Windows":
            cmake_args += ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}'.format(cfg.upper(), extdir)]
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
            build_args += ['--', '/m']
        else:
            cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
            build_args += ['--', '-j2']

        env = os.environ.copy()
        env['CXXFLAGS'] = '{} -DVERSION_INFO=\\"{}\\"'.format(
            env.get('CXXFLAGS', ''),
            self.distribution.get_version())
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args,
                              cwd=self.build_temp, env=env)
        subprocess.check_call(['cmake', '--build', '.'] + build_args,
                              cwd=self.build_temp)
        # Copy *_test file to tests directory
        dir_name = os.path.basename(ext.sourcedir) 
        test_bin = os.path.join(self.build_temp, dir_name + '_test')
        self.copy_test_file(test_bin)
        print() # Add empty line for nicer output

    def copy_test_file(self, src_file):
        """
        Copy ``src_file`` to `tests/bin` directory, ensuring parent directory
        exists. Messages like `creating directory /path/to/package` and
        `copying directory /src/path/to/package -> path/to/package` are
        displayed on standard output. Adapted from scikit-build.
        """

        # Create directory
        dest_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests', 'bin')
        print("Creating directory {}".format(dest_dir))
        try:
            os.makedirs(dest_dir, exist_ok=True)
        except IOError as e:
            raise RuntimeError(e)

        # Copy file
        dest_file = os.path.join(dest_dir, os.path.basename(src_file))
        print("Copying {} -> {}".format(src_file, dest_file))
        copyfile(src_file, dest_file)
        copymode(src_file, dest_file)


setup(
    name='deepland',
    version=__version__,
    url='',
    author='Adam Erickson',
    license=LICENSE,
    author_email='adam.erickson@wsu.edu',
    description='A framework for rapid prototyping of deep learning in LSMs',
    long_description='',
    # Tell setuptools to look for any packages under 'deepland'
    packages=find_packages(),
    # Tell setuptools that all packages will be under the 'deepland' directory
    # and nowhere else
    #package_dir={'':'deepland'},
    # Add an extension module named 'ops' to the package 'deepland'
    ext_modules=[
        CMakeExtension('deepland/ops'),
        CMakeExtension('deepland/classes')
    ],
    # Add custom build_ext command
    cmdclass=dict(build_ext=CMakeBuild),
    zip_safe=False,
    # Add test suite to run on build
    test_suite='tests',
    # General requirements
    python_requires='>=3',
    platforms='any'
)


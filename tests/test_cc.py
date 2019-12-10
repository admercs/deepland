import unittest
import subprocess
import os


class MainTest(unittest.TestCase):
    """Run C++ binary test program using unittest."""

    print("\nTesting C++ code... [blank == success]")

    def test_cc(self):
        
        command = os.path.join(os.path.dirname(os.path.relpath(__file__)),
                               'bin', 'deepland_test')
        subprocess.check_call(command)
        print() # for prettier output


if __name__ == '__main__':
    unittest.main()


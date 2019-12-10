import unittest

# pybind11 `ops` extension module from package `deepland`
from deepland import ops


class MainTest(unittest.TestCase):
    """Test ops module."""

    print("\nTesting Python code...")

    def test_add(self):
        # test that 1 + 1 = 2
        self.assertEqual(ops.add(1, 1), 2)

    def test_subtract(self):
        # test that 1 - 1 = 0
        self.assertEqual(ops.subtract(1, 1), 0)


if __name__ == '__main__':
    unittest.main()

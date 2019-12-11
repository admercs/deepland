import unittest

# pybind11 `ops` extension module from package `deepland`
from deepland import classes


class MainTest(unittest.TestCase):
    """Test classes module."""

    print("\nTesting Python code...")

    def test_first(self):
        # test initialization
        f = classes.First(5)
        self.assertEqual(f.get_number(), 5)

    def test_second(self):
        # test initialization
        s = classes.Second(10)
        s.set_id(1)

        self.assertEqual(s.get_id(), 1)
        self.assertEqual(s.get_number(), 10)


if __name__ == '__main__':
    unittest.main()

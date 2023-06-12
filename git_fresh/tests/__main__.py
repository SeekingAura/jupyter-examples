import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover(".")

    runner = unittest.TextTestRunner()
    runner.run(tests)

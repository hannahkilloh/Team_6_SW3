import unittest
import os


def run_tests():
    # Get the directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Define the directory where your test files are located
    tests_directory = os.path.join(script_directory, 'tests')

    # Discover and run all test files within the specified directory
    loader = unittest.TestLoader()
    suite = loader.discover(tests_directory)

    # Initialize a test runner
    runner = unittest.TextTestRunner()

    # Run the test suite
    result = runner.run(suite)

    # Return the test result
    return result


if __name__ == '__main__':
    test_result = run_tests()

    # Check if any test failed and exit with an appropriate status code
    if test_result.failures or test_result.errors:
        print("\n🔴🔴🔴 Tests failed 🔴🔴🔴")
        exit(1)
    else:
        print("\n🟢🟢🟢 All tests passed 🟢🟢🟢")
        exit(0)

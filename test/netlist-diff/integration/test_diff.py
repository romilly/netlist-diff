import subprocess
import unittest
from hamcrest import assert_that, contains_string


class DiffTestCase(unittest.TestCase):
    def test_identical_files_have_no_differences(self):
        result = subprocess.run(['python3',
                                 'src/netlist_diff/diff.py',
                                 'test/data/file1.xml',
                                 'test/data/file2.xml',
                                 ],
                                capture_output=True)
        self.assertEqual(result.returncode, 0)
        assert_that(result.stdout.decode('UTF8'), contains_string('No difference'))


if __name__ == '__main__':
    unittest.main()

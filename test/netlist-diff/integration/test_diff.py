import subprocess
import unittest
from hamcrest import assert_that, contains_string


class DiffTestCase(unittest.TestCase):
    def test_identical_files_have_no_differences(self):
        result = subprocess.run(['python3',
                                 'src/netlist_diff/diff.py',
                                 'test/data/555_netlist.xml',
                                 'test/data/555_netlist.xml',
                                 ],
                                capture_output=True)
        if result.returncode != 0:
            raise ValueError(result.stderr)
        assert_that(result.stdout.decode('UTF8'), contains_string('No difference'))

    def test_detects_files_that_differ(self):
        result = subprocess.run(['python3',
                                 'src/netlist_diff/diff.py',
                                 'test/data/555-stripboard_netlist.xml',
                                 'test/data/555_netlist.xml',
                                 ],
                                capture_output=True)
        if result.returncode != 0:
            raise ValueError(result.stderr)
        assert_that(result.stdout.decode('UTF8'), contains_string('differ'))


if __name__ == '__main__':
    unittest.main()

import subprocess
import unittest
from hamcrest import assert_that, contains_string


class DiffTestCase(unittest.TestCase):
    def look_for_output(self, source, target, expected_item):
        result = subprocess.run(['python3',
                                 'src/netlist_diff/diff.py',
                                 source,
                                 target,
                                 ],
                                capture_output=True)
        if result.returncode != 0:
            raise ValueError(result.stderr)
        assert_that(result.stdout.decode('UTF8'), contains_string(expected_item))

    def test_identical_files_have_no_differences(self):
        expected_item = 'No difference'
        self.look_for_output('test/data/555_netlist.xml',
                             'test/data/555_netlist.xml',
                             expected_item)

    def test_detects_files_that_differ(self):
        expected_item = 'differ'
        self.look_for_output('test/data/555-stripboard_netlist.xml',
                              'test/data/555_netlist.xml',
                            expected_item)

    def test_identifies_missing_components(self):
        # TODO: tighten test, add unit tests, refactor names in diff code
        expected_item = 'Generic female header - 2 pins'
        self.look_for_output('test/data/555-stripboard_netlist.xml',
                             'test/data/555_netlist.xml',
                             expected_item)


if __name__ == '__main__':
    unittest.main()

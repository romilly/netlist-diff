import unittest

from netlist_diff.component_finder import ComponentFinder
from test.netlist_diff.helpers.sample_data import NETLIST_FOR_555_BREADBOARD
from hamcrest import assert_that, equal_to


class ComponentFinderTestCase(unittest.TestCase):
    def test_finds_component_counts(self):
        finder = ComponentFinder()
        parts_dict = finder.components_in(NETLIST_FOR_555_BREADBOARD)
        self.assertTrue('555 Timer' in parts_dict.keys())
        assert_that(len(parts_dict['555 Timer']), equal_to(1))


if __name__ == '__main__':
    unittest.main()

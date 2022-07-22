import sys
from io import StringIO

from netlist_diff.component_finder import ComponentFinder


def read(path):
    with open(path) as sf:
        return sf.read()


class ComponentDiffer:
    def diff_components(self, diff, source_components, target_components):
        for key in source_components.keys():
            if key not in target_components.keys():
                diff.write('%s is in left but not in right\n' % key)


def diff_component_dicts(diff, source_components, target_components):
    differ = ComponentDiffer()
    differ.diff_components(diff, source_components, target_components)


def diff_text(source, source_content, target, target_content):
    component_finder = ComponentFinder()
    if source_content == target_content:
        return('No difference between %s and %s' % (source, target))
    else:
        diff = StringIO()
        diff.write('%s and %s differ\n' % (source, target))
        source_components = component_finder.components_in(source_content)
        target_components = component_finder.components_in(target_content)
        diff_component_dicts(diff, source_components, target_components)
    result = diff.getvalue()
    diff.close()
    return result


def diff(source, target):
    source_content = read(source)
    target_content = read(target)
    print(diff_text(source, source_content, target, target_content))


if __name__ == '__main__':
    _, source, target = sys.argv
    diff(source, target)
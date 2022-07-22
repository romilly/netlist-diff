import sys


def read(source):
    with open(source) as sf:
        return sf.read()


def diff_text(source, source_content, target, target_content):
    if source_content == target_content:
        return('No difference between %s and %s' % (source, target))
    else:
        return('%s and %s differ' % (source, target_content))


def diff(source, target):
    source_content = read(source)
    target_content = read(target)
    print(diff_text(source, source_content, target, target_content))


if __name__ == '__main__':
    _, source, target = sys.argv
    diff(source, target)
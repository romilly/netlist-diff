import sys


def diff(source, target):
    print('No difference')


if __name__ == '__main__':
    _, source, target = sys.argv
    diff(source, target)
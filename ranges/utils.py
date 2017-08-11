import itertools


def intervals(l):
    return zip(l, l[1:])

def combine(*ranges):
    combinations = itertools.product(*ranges)
    return map(iter, combinations)

from .types import Step
from .parse import parse
from . import utils
from . import date


def values(r, string=False):
    if string:
        return [utils.unicode(v) for v in r]
    else:
        return [v.value for v in r]


# calculates stop from start, or vice versa, no intermediate steps,
# only for dates, letters and numbers
def interval(start, **options):
    raise NotImplementedError()


# a space is like a range, but with a number of steps (based on which the
# appropriate step size is then constructed) rather than a step size
def space(start, stop, num):
    return range()


# TODO: `step` for floats and dates, if not defined, should be
# dynamic based on the granularity of `start`
# e.g. 2013-03 ==> +1M
# e.g. 1.23 ==> +0.01
# e.g. 2H ==> +1H
#
# TODO: `n` argument, so e.g. you specify start and n=10
# and it will increment 9 times
def range(start, stop, step=None, closed=False, string=False, intervals=False, **options):
    """
    This function is (or should be) a strict superset of the `range`
    builtin and so can be safely loaded as `from ranges import range`.

    Negative steps should be supported too.

    Steps can be numbers (translates to skips in the range) or
    strings (e.g. 'minute', 'day', ...)
    """

    start = Step.cast(start)
    stop = Step.cast(stop)
    step = Step.cast(step)

    if start.__class__.__name__ != stop.__class__.__name__:
        raise ValueError()

    # a stepless range can be useful if we simply wish to
    # cast the start and stop values from strings into
    # a more appropriate type
    if step is False:
        return values([start, stop], string)

    r = start.to(stop, step)

    # all Step#to methods should return a closed range,
    # so if an open range is demanded, we just chop
    # off the last value
    if not closed:
        r = r[:-1]

    # we can return the range's values in string format
    # we were given, or cast into the proper types
    r = values(r, string)

    # intervals are pairs, e.g. (a, b) (b, c) (c, d)
    if intervals:
        r = utils.intervals(r)

    return r

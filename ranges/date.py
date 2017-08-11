from dateutil.relativedelta import relativedelta
from funcy import pairwise


def interval(start=None, stop=None, **offsets):
    delta = relativedelta(**offsets)

    if start:
        return (start, start + delta)
    elif stop:
        return (stop - delta, stop)
    else:
        raise ValueError()

def range(start, stop, align=False, alignment='left', closed=False, intervals=None, **offsets):
    """
    * days, weeks, months and years interval
    * align means you "snap" the daterange to the nearest start of the week/month/year etc.;
      with alignment, you decide whether to snap to the next valid occurence, or the previous one.
      e.g. `align="day"`
    * intervals is similar to step, but returns (start, stop) pairs for every step
    * a closed interval includes both start and stop
    """

    # TODO: incorporate alignment
    steps = []
    last = start

    delta = relativedelta(**offsets)

    while last < stop:
        yield last
        last = last + delta

    if closed:
        yield last

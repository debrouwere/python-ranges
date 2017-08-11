"""
Also see 

https://pypi.python.org/pypi/RangeParser
(parse ranges like 10,20,30-50)
https://pypi.python.org/pypi/DateRangeParser
(parse ranges like 10-17 January, March 2014 - May 2015)
http://pythonhosted.org//ranger/tutorial/ranges.html#using-range-objects
(operations on ranges: intersection, span, difference, contains, contains all, 
overlaps, union etc. w/ both continuous and discrete [stepped] ranges)
(additionally, using these basic operations, it makes available a 
range map [any key between x-y => value] and range bucket [any key between
x-y => any corresponding values])
https://pypi.python.org/pypi/multirange
(return the gaps in ranges, a.k.a. the inverse of a range of discrete values)
https://github.com/brianhicks/cowboy
(uses operator overloading to enable `value in range` comparisons)
https://pypi.python.org/pypi/lrange/0.0.5
(lazy infinite ranges, like xrange)
https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence
(abstract base class for sequences)
https://github.com/zacharyvoase/daterange/
(date ranges)
https://pypi.python.org/pypi/datetimes/
(date ranges using timedelta for intervals)
"""

def pad(l, n, value):
    l = list(l)
    while len(l) < n:
        l.append(value)
    return l

# TODO: use `ranges` under the hood, so we can do more kinds of ranges
# TODO: support ranges that combine , and .., e.g. `3,4,5..10..2`
# to produce `3,4,5,7,9`
# TODO: distinguish between closed ranges (..) and open ranges (...)
def parse(description, 
    sequence_delimiters=[','], 
    closed_range_delimiters=['..', ' - '], 
    open_range_delimiters=['...', ' -- '], 
    step_delimiters=['..', '/']):

    if ',' in description:
        return description.split(',')
    elif '..' in description:
        params = description.split('..')
        start, stop, step = map(int, pad(params, n=3, value=1))
        return range(start, stop, step)
    else:
        raise ValueError()

`ranges` generates various kinds of ranges, either in whatever Python data type is appropriate or as a list of strings that retain all the various quirks of your start, stop and step arguments.

    # the range function is a strict superset of the Python builtin
    >>> from ranges import range
    >>> range('2013-02.01', '2013-02.03')
    ['2013-02.01', '2013-02.02', '2013-02.03']
    >>> range('10H13M', '10H17M', step=2, closed=True)
    ['10H13M', '10H15M', '10H17M']
    >>> range('0000', '0500', 100)
    ['0000', '0100', '0200', '0300', '0400']

`ranges` will e.g. return dates in exactly the format you gave it, integers with the same amount of zero-padding and so on. It accepts strings as arguments and figures out what kind of range you need by itself.

This makes it uniquely suitable for fetching a range of related files in a format you have no control over.

But of course `ranges` is equally good for just regular ranges:

    >>> from datetime import date
    >>> from ranges import range
    >>> range(date(2013,1,1), date(2013,1,3))
    ...
    >>> range(0, 10, 3)
    [0, 3, 6, 9]
    >>> range(9.2, 10.0, 0.25)
    [9.2, 9.45, 9.7, 9.95]

* date ranges
* time ranges
* datetime ranges
* number ranges (like Python's `range`)
* letter ranges

In addition to ranges, it is also possible to generate spaces: ranges with a
predetermined amount of equally spaced steps, rather than an explicit step size.

When and how to use
===================

`ranges`, when given string inputs, essentially tries to guess what those inputs signify and create ranges from those guesses. While pretty reliable, it is advisable to only use guesses when the user or developer experience absolutely requires this. For generating ranges that are not seen by anything other than the computer, you're better off supplying `range` with the appropriate data types.

    >>> from datetime import date
    >>> from hrange import range
    # better when responding to user input etc.
    range('2013-01-05', '2013-01-10')
    # better for programmatic use
    >>> range(date(2013,1,1), date(2013,1,3))

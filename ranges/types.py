import datetime
import re
import string
from collections import OrderedDict

# Python 2/3 compatibility
try:
    basestring = basestring
    unicode = unicode
except NameError:
    basestring = str
    unicode = str

try:
    import __builtin__ as builtins
except ImportError:
    import builtins


class Step(object):
    @classmethod
    def cast(self, raw):
        for cls in [Integer, Float, Character, Date]:
            if cls.match(raw):
                return cls(raw)
        return raw

    def __init__(self, raw):
        self.raw = raw


class Integer(Step):
    def __init__(self, raw, width=None):
        self.raw = raw

        if isinstance(raw, basestring):
            self.value = int(raw)
            if width is None and raw.startswith('0'):
                width = len(raw)
        else:
            self.value = raw

        self.width = width or 0

    @classmethod
    def match(cls, value):
        is_int = isinstance(value, int)
        is_numeric = isinstance(value, basestring) and re.match(r'^[0-9]+$', value)
        return is_int or is_numeric

    def to(self, stop, step):
        r = builtins.range(self.value, stop.value, step.value) + [stop]
        return [Integer(v, self.width) for v in r]

    def __unicode__(self):
        return unicode(self.value).zfill(self.width)


class Float(Integer):
    def __init__(self, raw, width=None, decimals=None):
        self.raw = raw
        if isinstance(raw, basestring):
            self.value = float(raw)
            if width is None:
                if raw.startswith('0') or raw.endswith('0'):
                    width = len(raw)
                    decimals = len(raw.split('.')[1])
        else:
            self.value = raw

        self.width = width or 0
        self.decimals = decimals

    @classmethod
    def match(cls, value):
        is_float = isinstance(value, float)
        is_numeric = isinstance(value, basestring) and re.match(r'^[0-9]+\.[0-9]+$', value)
        return is_float or is_numeric

    def to(self, other, step):
        r = [self]
        while r[-1].value < other.value:
            v = Float(r[-1].value + step.value, self.width, self.decimals)
            r.append(v)

        return r

    def __unicode__(self):
        right = self.decimals

        if right is None:
            value = self.value
        else:
            value = round(self.value, right)

        integer, fractional = unicode(value).split('.')
        fractional = fractional.ljust(right, '0')
        value = ".".join((integer, fractional))
        return value.zfill(self.width)


class Character(Step):
    def __init__(self, raw):
        self.raw = self.value = raw
        if raw.islower():
            self.case = string.lowercase
        else:
            self.case = string.uppercase

    @classmethod
    def match(cls, value):
        return isinstance(value, basestring) and re.match(r'^[a-zA-Z]{1}$', value)

    @property
    def ix(self):
        return self.case.index(self.value)

    def to(self, other, step):
        r = range(self.ix, other.ix, step) + [other.ix]
        return [Character(self.case[ix]) for ix in r]

    def __unicode__(self):
        return unicode(self.value)


class Date(Step):
    """
    We're going to do this without dateutil, because
    we need to preserve the initial format so we can
    output a formatted date at the end of the ride.

    Supported formats:

    - YYYY
    - YYYY-MM
    - YYYY-MM-DD
    - MM-DD

    - HH:MM

    - combination of the above

    (Only years, months etc. are not supported:
    these would count as regular integer-based ranges.
    Shorthand years are not supported either: these
    would be ambigous and could be interpreted as months.)

    Supported separators are dash, dot, underscore
        - . _
    """

    multipliers = {
        'S': 1,
        'M': 60,
        'H': 60 * 60,
        'D': 60 * 60 * 24,
        'W': 60 * 60 * 24 * 7,
        'Y': 60 * 60 * 24 * 365,
    }

    components = OrderedDict((
        ('year', r"([0-9]{4})"),
        ('ym', r"([\-\.\_\ \\])"),
        ('month', r"([0-9]{2})"),
        ('md', r"([\-\.\_\ \\])"),
        ('day', r"([0-9]{2})"),
        ('dt', r"([\-\.\_\ \\])"),
        ('hour', r"([0-9]{2})"),
        ('hm', r"([Hh\:\-\.\_\ \\])"),
        ('minute', r"([0-9]{2})"),
        ('ms', r"([Mm])"),
        ('second', r"([0-9]{2})"),
        ('s', r"([Ss])"),
    ))

    formats = OrderedDict((
        ('year', '%Y'),
        ('month', '%m'),
        ('day', '%d'),
        ('hour', '%H'),
        ('minute', '%M'),
        ('second', '%s'),
    ))

    pattern = r"""
        ^
        ({year}{ym}?{month}{md}?{day}|{year}{ym}?{month}|{month}{md}?{day})?
        {dt}?
        ({hour}{hm}?{minute}{ms}?({second}{s})?)?
        $
        """.format(**components)

    pattern = re.compile(pattern, re.VERBOSE)

    # Python doesn't allow repeating group names (even if mutually exclusive)
    # so we have to resort to this kind of silliness to make sense of our RegEx.
    groups = [
        'year', 'ym', 'month', 'md', 'day',
        'year', 'ym', 'month',
        'month', 'md', 'day',
        'dt',
        '_time',
        'hour', 'hm', 'minute', 'ms', '_second', 'second', 's'
        ]


    @classmethod
    def match(cls, value):
        if cls._is_date(value):
            return True
        elif isinstance(value, basestring) and re.match(cls.pattern, value):
            return True
        else:
            return False

    @classmethod
    def _is_date(cls, value):
        d = isinstance(value, datetime.date)
        t = isinstance(value, datetime.time)
        dt = isinstance(value, datetime.datetime)
        return d or t or dt

    def __init__(self, raw, format=None):
        self.raw = raw

        if format:
            self._format = format
        else:
            matches = list(re.match(self.pattern, raw).groups()[1:])
            tuples = zip(self.groups, matches)
            self._format = dict([(k, v) for k, v in tuples if v])

        if self._is_date(raw):
            self.value = raw
        else:
            # extract date and time
            self.value = self._parse_date(self._format)

    def _parse_date(self, format):
        year = int(format.get('year', 9999))
        month = int(format.get('month', 1))
        day = int(format.get('day', 1))
        hour = int(format.get('hour', 0))
        minute = int(format.get('minute', 0))
        second = int(format.get('second', 0))

        if 'month' in format and '_time' in format:
            return datetime.datetime(year, month, day, hour, minute, second)
        elif 'month' in format:
            return datetime.datetime(year, month, day)
        elif '_time' in format:
            return datetime.datetime(9999, 1, 1, hour, minute, second)
        else:
            raise ValueError()

    def _parse_step(self, step):
        if isinstance(step, basestring):
            magnitude = step[:-1]
            unit = step[-1:].upper()
            step = float(magnitude) * self.multipliers[unit]

        return datetime.timedelta(seconds=step)

    @property
    def format(self):
        date_components = self.formats.keys()
        components = [c for c in self.components]
        first = next(c for c in date_components if c in self._format)
        last = next(c for c in reversed(date_components) if c in self._format)
        start = components.index(first)
        stop = components.index(last) + 1

        fmt = ''
        for component in components[start:stop]:
            # replace date components with strftime placeholders
            if component in date_components and component in self._format:
                fmt += self.formats[component]
            # keep the original separators intact
            else:
                fmt += self._format.get(component, '')

        return fmt

    def to(self, other, step):
        step = self._parse_step(step)

        r = [self]
        while r[-1].value < other.value:
            r.append(Date(r[-1].value + step, self._format))

        return r

    def __unicode__(self):
        return self.value.strftime(self.format)

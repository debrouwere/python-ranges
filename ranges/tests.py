import unittest
import ranges


def TestRange(unittest.TestCase):
    """ Test ranges of simple Python data types. """

    def test_int(self):
        """ We can generate a range of integers. """

        """
        >>> range(0, 10, 3)
        [0, 3, 6, 9]
        """

        raise NotImplementedError()

    def test_closed_int(self):
        """ We can generate a closed range of integers. """
        raise NotImplementedError()

    def test_float(self):
        """ We can generate a range of floats. """

        """
        >>> range(9.2, 10.0, 0.25)
        [9.2, 9.45, 9.7, 9.95]
        """

        raise NotImplementedError()

    def test_closed_float(self):
        """ We can generate a closed range of floats. """
        raise NotImplementedError()

    def test_character(self):
        """ We can generate a range of characters. """
        raise NotImplementedError()

    def test_closed_characters(self):
        """ We can generate a closed range of characters. """
        raise NotImplementedError()

    def test_date(self):
        """ We can generate a range of dates. """

        """
        >>> range(date(2013,1,1), date(2013,1,3))
        ...
        """

        raise NotImplementedError()

    def test_closed_date(self):
        """ We can generate a closed range of dates. """
        raise NotImplementedError()

    def test_time(self):
        """ We can generate a range of times. """
        raise NotImplementedError()

    def test_closed_time(self):
        """ We can generate a closed range of times. """
        raise NotImplementedError()

    def test_datetime(self):
        """ We can generate a range of datetimes. """
        raise NotImplementedError()

    def test_closed_datetime(self):
        """ We can generate a closed range of datetimes. """
        raise NotImplementedError()


def TestHRange(unittest.TestCase):
    """ Test complex ranges based on string definitions. """

    def test_int(self):
        """ We can generate a range of integers from strings. """
        raise NotImplementedError()

    def test_padded_int(self):
        """ We can generate a range of padded integers from strings. """

        """
        >>> range('0000', '0500', 100)
        ['0000', '0100', '0200', '0300', '0400']
        """

        raise NotImplementedError()

    def test_closed_padded_int(self):
        """ We can generate a closed range of padded integers from strings. """
        raise NotImplementedError()

    def test_float(self):
        """ We can generate a range of floats from strings. """
        raise NotImplementedError()

    def test_padded_float(self):
        """ We can generate a range of padded floats from strings. """
        raise NotImplementedError()

    def test_rounded_float(self):
        """ We can generate a range of rounded floats from strings. """
        raise NotImplementedError()

    def test_padded_rounded_float(self):
        """ We can generate a range of padded and rounded floats from strings. """
        raise NotImplementedError()

    def test_closed_padded_rounded_float(self):
        """ We can generate a closed range of padded and rounded floats from strings. """
        raise NotImplementedError()

    def test_date(self):
        """ We can generate a range of dates that respect the original string formatting. """

        """
        >>> range('2013-02.01', '2013-02.03')
        ['2013-02.01', '2013-02.02', '2013-02.03']
        """

        raise NotImplementedError()

    def test_closed_date(self):
        """ We can generate a closed range of dates from strings. """
        raise NotImplementedError()

    def test_time(self):
        """ We can generate a range of times that respect the original string formatting. """

        """
        >>> range('10H13M', '10H17M', step=2, closed=True)
        ['10H13M', '10H15M', '10H17M']
        """

        raise NotImplementedError()

    def test_closed_time(self):
        """ We can generate a closed range of times from strings. """
        raise NotImplementedError()

    def test_datetime(self):
        """ We can generate a range of datetimes that respect the original string formatting. """
        raise NotImplementedError()

    def test_closed_date(self):
        """ We can generate a closed range of datetimes from strings. """
        raise NotImplementedError()




# tests, until we get a setup.py sorted out etc.
if __name__ == '__main__':
    print range(0, 10, 2)
    print range('00', '10', 2, string=True)
    print range('1.100', '1.650', 0.175, string=False)
    print range('1.100', '1.650', 0.175, string=True)
    print range('A', 'H', 1)
    print range('a', 'H', 2)
    print range('2013-12 11:00', '2013-12 11:21', '3M', string=True)
    print range('2013-12-31 23:55', '2014-01-01 00:10', '10M', string=True)

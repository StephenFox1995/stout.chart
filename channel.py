# coding=utf-8

__author__ = "Stephen Fox"


# Base class for any channel objects.
class Channel(object):
    """
    Construct a new `Channel` object.
    :param tag: The name of the channel
    :type tag: str

    :param height The height of the channel.
    :type height: int

    :param value: The value of the channel.
    :type value: int

    :param delimeter: The character to use for charting.
    :typer delimeter: str
    """
    def __init__(self, tag, height, value, delimeter="█"):
        self._tag = tag
        self._height = height
        self._value = value
        self._delimeter = delimeter
        self._output = ""

    def __str__(self):
        return self._output

    @property
    def tag(self):
        return self._tag

    @property
    def value(self):
        return self._value


# Represents a channel which is drawn horizontally.
class HorizontalChannel(Channel):
    def __init__(self, tag, height, value, delimeter="█"):
        super(HorizontalChannel, self).__init__(tag, height, value, delimeter)
        self.__generate_output()

    def __generate_output(self):
        self._output += "%s| " % self._tag
        for x in range(0, self._height):
            if x < self._value:
                self._output += self._delimeter
            else:
                self._output += " "

    def __str__(self):
        return self._output

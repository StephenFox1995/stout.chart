import numpy as np
from random import randint

__author__ = "Stephen Fox"


class Chart(object):
    def __init__(self, plot_height, plot_width):
        self._plot_height = plot_height
        self._plot_width = plot_width
        self._channels = np.chararray((plot_height, plot_width), unicode=True)

    def render(self):
        if len(self._channels) == 0 or self._channels is None:
            raise ValueError("Cannot render %s, no %s's set." % (
                type(self), 
                Chart.Channel
            ))

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, channels):
        for channel in channels:
            self._channels = np.append(self._channels, channel.matrix)

    @property
    def width(self):
        return self._plot_width

    @property
    def height(self):
        return self._plot_height

    def __str__(self):
        return "".join(["%s\n" % str(x) for x in self._channels])

    class Channel(object):
        """
        Construct a new `Channel` object.
        :param chart: The chart to which the instance will be added to.
        :type chart: `Chart`

        :param height The height of the channel.
        :type height: int

        :param width: The width of the channel.
        :type width: int

        :param value: The value of the channel.
        :type value: int
        """
        def __init__(self, chart, height, width, value):
            self._height = height
            self._width = width
            # No need to keep permanent reference chart, just do check.
            self.__fail_if_chart_plot_too_small(chart)
            self._value = value
            self.__matrix = np.chararray((height, width), unicode=True)
            self.__generate_matrix()

        """Fail if the chart is too small to plot the channel."""
        def __fail_if_chart_plot_too_small(self, chart):
            if self._width > chart.width or self._height > chart.height:
                raise ValueError("Chart size is too small for %s size (%d, %d) > (%d, %d)" % (
                    type(self),
                    (self._width, self._height),
                    (chart.width, chart.width)
                ))

        def __generate_matrix(self):
            for i in range(self._value):
                self.__matrix[i:] = ("█", )*self._width

        @property
        def matrix(self):
            return self.__matrix

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value

        def __str__(self):
            return str(self.__matrix)
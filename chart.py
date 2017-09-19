class Chart(object):
    def __init__(self, channels, heading=""):
        self._lines = []  # All lines that will be printed.
        self._channels = []
        self._heading = "| %s |" % heading
        self._lines.append(heading)
        self._values = ""
        self._max_tag_indent = 0
        for channel in channels:
            self._channels.append(channel)
            self._lines.append(channel)
            self._values += "%s, " % str(channel.value)
            if len(channel.tag) > self._max_tag_indent:
                self._max_tag_indent = len(channel.tag)
        self._lines.append(self._values)

    def __iter__(self):
        return iter(self._lines)





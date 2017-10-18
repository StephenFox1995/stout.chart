class Chart(object):

    # Param keys.
    FG_COLOR = "fg_color"
    BG_COLOR = "bg_color"
    HEADING = "heading"

    def __init__(self, channels, **kwargs):
        self._fg_color = "red"
        self._bg_color = "reset"
        self._heading = "stout.chart"
        self._lines = []  # All lines that will be printed.
        self._channels = channels

        if self.FG_COLOR in kwargs and kwargs.get(self.FG_COLOR) is not None:
            self._fg_color = kwargs.get(self.FG_COLOR)
        if self.BG_COLOR in kwargs and kwargs.get(self.BG_COLOR) is not None:
            self._bg_color = kwargs.get(self.BG_COLOR)
        if self.HEADING in kwargs and kwargs.get(self.HEADING) is not None:
            self._heading = kwargs.get(self.HEADING)

        self._heading = "| %s |" % self._heading
        self._lines.append(self._heading)

        max_tag_indent = self._find_max_tag_indent_needed()
        for channel in self._channels:
            indent_more_by = (len(channel.tag) - max_tag_indent) * -1
            line = "%s%s |%s" % (channel.tag,
                                 " "*indent_more_by,
                                 str(channel))
            self._lines.append(line)

    # Find the max indentation needed for all channel tags.
    def _find_max_tag_indent_needed(self):
        max_indent = 0
        for channel in self._channels:
            if len(channel.tag) > max_indent:
                max_indent = len(channel.tag)
        return max_indent

    def __iter__(self):
        return iter(self._lines)

    @property
    def fg_color(self):
        return self._fg_color

    @property
    def bg_color(self):
        return self._bg_color


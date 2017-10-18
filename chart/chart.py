class Chart(object):
    def __init__(self, channels, heading=""):
        self._lines = []  # All lines that will be printed.
        self._channels = channels
        self._heading = "| %s |" % heading
        self._lines.append(heading)

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

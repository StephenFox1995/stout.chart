import re

import click

from chart.channel import HorizontalChannel
from chart.chart import Chart

__author__ = "Stephen Fox"


def generate_chart(data, **kwargs):
    channels = []
    matches = re.finditer(r"(?:\s)?(?P<key>[\D]+)(?:\s|:)+(?=[0-9]+)(?P<value>[0-9]+)", data)
    for match in matches:
        key = match.group("key")
        value = match.group("value")
        channels.append(HorizontalChannel(key, int(value), int(value)))
    return Chart(channels, **kwargs)


def static_output(chart):
    for line in chart:
        click.secho(line, bg=chart.bg_color, fg=chart.fg_color)


@click.command()
@click.option("-d", "--data",
              type=str,
              help="Key value pair: spaced e.g. ireland 50 united kingdom 43")
@click.option("-h", "--heading",
              type=str,
              help="Heading for the outputted data.")
@click.option("-fg", "--fgcolor",
              type=click.Choice(['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']))
@click.option("-bg", "--bgcolor",
              type=click.Choice(['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']))
def main(data, heading, fgcolor, bgcolor):
    static_output(generate_chart(data, heading=heading, fg_color=fgcolor, bg_color=bgcolor))


if __name__ == "__main__":
    main()

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
        click.secho(line, fg=chart.color)


@click.command()
@click.option("-d", "--data",
              type=str,
              help="Key value pair: spaced e.g. ireland 50 united kingdom 43")
@click.option("-h", "--heading",
              type=str,
              help="Heading for the outputted data.")
@click.option("-c", "--color",
              type=click.Choice(['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']))
def main(data, heading, color):
    static_output(generate_chart(data, heading=heading, color=color))


if __name__ == "__main__":
    main()

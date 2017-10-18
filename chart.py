import re

import click

from chart.channel import HorizontalChannel
from chart.chart import Chart

__author__ = "Stephen Fox"


def generate_chart(data, heading):
    channels = []
    matches = re.finditer(r"(?:\s)?(?P<key>[\D]+)(?:\s|:)+(?=[0-9]+)(?P<value>[0-9]+)", data)
    for match in matches:
        key = match.group("key")
        value = match.group("value")
        channels.append(HorizontalChannel(key, int(value), int(value)))
    return Chart(channels, heading)


def static_output(chart):
    for line in chart:
        click.secho(line, fg="red")


@click.command()
@click.option("-d", "--data",
              type=str,
              help="Key value pair: spaced e.g.")
@click.option("-h", "--heading",
              type=str,
              help="Heading for the outputted data.")
def main(data, heading):
    static_output(generate_chart(data, heading))


if __name__ == "__main__":
    main()

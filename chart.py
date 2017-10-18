import re

import click

from chart.channel import HorizontalChannel
from chart.chart import Chart

__author__ = "Stephen Fox"


def generate_chart(data, heading):
    matches = re.finditer(r"(.+[^0-9])([0-9]+)", data)
    for match in matches:
        tags = match.start()
        value = match.end()
        print("start:%s end:%s" % (tags, value))
        return
    tags = re.findall(r"([a-zA-Z]+)", data)
    values = re.findall(r"[0-9]+", data)
    if len(tags) != 0:
        # todo: assumes all values will have corresponding tags
        channels = [HorizontalChannel(tag, int(val), int(val)) for tag, val in zip(tags, values)]
    else:
        channels = [HorizontalChannel("", int(x), int(x)) for x in data.split(" ")]
    return Chart(channels, heading)


def static_output(chart):
    for line in chart:
        click.secho(line, fg="red")


@click.command()
@click.option("-d", "--data",
              type=str,
              help="Comma separated values. e.g. -d 1, 2, 3, 10")
@click.option("-h", "--heading",
              type=str,
              help="Heading for the outputted data.")
def main(data, heading):
    static_output(generate_chart(data, heading))


if __name__ == "__main__":
    main()
import click
from reprint import output
from channel import HorizontalChannel
from chart import Chart
from random import randint

__author__ = "Stephen Fox"


def generate_chart(data, heading):
    channels = [HorizontalChannel("", int(x), int(x)) for x in data.split(" ")]
    return Chart(channels, heading)


def static_output(chart):
    for line in chart:
        click.echo(line)


# Draw the chart/ channels dynamically.
def dynamic_output():
    with output(initial_len=3, interval=100) as output_lines:
        while True:
            output_lines[0] = str(HorizontalChannel("100mhz", 20, randint(1, 19)))
            output_lines[1] = str(HorizontalChannel("120mhz", 30, randint(1, 29)))
            output_lines[1] = str(HorizontalChannel("120mhz", 30, randint(1, 15)))


@click.command()
@click.option("--dynamic",
              is_flag=True,
              help="Displays the chart dynamically.")
@click.option("-d", "--data",
              type=str,
              help="Comma separated values. e.g. -d 1, 2, 3, 10")
@click.option("-h", "--heading",
              type=str,
              help="Heading for the outputted data.")
def main(dynamic, data, heading):
    if dynamic:
        click.echo("Y u du diz?")
        return 0
    static_output(generate_chart(data, heading))


if __name__ == "__main__":
    main()

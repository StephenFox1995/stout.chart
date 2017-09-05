import time
import random
from reprint import output
from chart import Chart

n = 5
chart = Chart(n, n*2)
with output(initial_len=n*2, interval=0) as output_lines:
    while True:
        for i, row in enumerate(chart.matrix):
            _str = ""
            for col in row:
                _str = _str + str(col.decode())
            output_lines[i] = _str
        time.sleep(0.3)
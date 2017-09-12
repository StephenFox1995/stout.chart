import time
import random
from reprint import output
from chart import Chart

n = 1
chart = Chart(10, 10)
channels = [Chart.Channel(chart, height=5, width=2, value=1) for channel in range(0, 1)]
chart.channels = channels
chart.render()
print(chart)
# for i, row in enumerate(chart.ma)
# with output(initial_len=n*2, interval=0) as output_lines:
#     while True:
#         pass
        # for i, row in enumerate(chart.matrix):
        #     _str = ""
        #     for col in row:
        #         _str = _str + str(col.decode())
        #     output_lines[i] = _str
        # time.sleep(0.3)
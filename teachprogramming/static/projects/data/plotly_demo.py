"""
* [Plotly](https://plot.ly/) [Simple Scatter Example](https://plot.ly/python/line-and-scatter/#simple-scatter-plot)
    * [Falcon](https://github.com/plotly/falcon) Plotly can work directly from SQL DB's
"""

import random
import plotly

N = 1000
scatter = plotly.graph_objs.Scatter(
    x = [random.randint(0,N) for x in range(N)],
    y = [random.randint(0,N) for y in range(N)],
    mode = 'markers'
)

plotly.offline.plot([scatter], filename='basic-scatter.html', auto_open=False)

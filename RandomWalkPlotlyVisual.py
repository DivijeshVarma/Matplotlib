import plotly.graph_objects as go
import numpy as np
from RandomWalkPlotly import RandomWalk

while True:

    walk = RandomWalk()
    walk.fill_walk()

    fig = go.Figure(data=go.Scatter(
        x=walk.x_values,
        y=walk.y_values,
        mode='markers',
        name='Random Walk',
        marker=dict(
            color=np.arange(walk.num_points),
            size=9,
            colorscale='Blues',
            showscale=True
        )
    ))

    fig.show()

    response = input('continue Random walk y/n: ')
    if response == 'n':
        break

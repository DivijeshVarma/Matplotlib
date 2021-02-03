import matplotlib.pyplot as plt
from RandomWalk import RandomWalk

while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(18, 9), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)
    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=80)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=80)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.tight_layout()
    plt.show()

    response = input('continue Random walk y/n: ')
    if response == 'n':
        break

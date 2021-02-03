import matplotlib.pyplot as plt
from RandomWalk import RandomWalk

while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)

    plt.show()

    response = input('continue Random walk y/n: ')
    if response == 'n':
        break

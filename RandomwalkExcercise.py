# 15-3. Molecular Motion: Modify rw_visual.py by replacing plt.scatter() with plt.plot().
# To simulate the path of a pollen grain on the surface of a drop of water, pass in the rw.x_values and rw.y_values,
# and include a line width argument. Use 5000 instead of 50,000 points.

import matplotlib.pyplot as plt
from RandomWalk import RandomWalk

while True:
    # Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(18, 9), dpi=128)
    ax.plot(rw.x_values, rw.y_values, color='cyan', linewidth=3, zorder=1)
    # The scatter plots appear behind the lines. To place them on top of the lines, we can use the zorder argument.
    # Plot elements with higher zorder values are placed on top of elements with lower zorder values.

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=80, zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=80, zorder=2)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.tight_layout()
    plt.show()

    response = input('continue Random walk y/n: ')
    if response == 'n':
        break

# 15-4. Modified Random Walks: In the RandomWalk class, x_step and y_step are generated from the same set of conditions.
# The direction is chosen randomly from the list [1, -1] and the distance from the list [0, 1, 2, 3, 4].
# Modify the values in these lists to see what happens to the overall shape of your walks.
# Try a longer list of choices for the distance, such as 0 through 8, or remove the −1 from the x or y direction list.
#
# x_direction = choice([1])
# x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
# x_step = x_direction * x_distance
#
# y_direction = choice([1, -1])
# y_distance = choice([0, 1, 2, 3, 4, 5, 6])
# y_step = y_direction * y_distance

# 15-5. Refactoring: The fill_walk() method is lengthy. Create a new method called get_step() to determine the direction
# and distance for each step, and then calculate the step.
# You should end up with two calls to get_step() in fill_walk(): x_step = self.get_step() y_step = self.get_step()
# This refactoring should reduce the size of fill_walk() and make the method easier to read and understand.

    # def fill_walk(self):
    #     """Calculate all the points in the walk."""
    #
    #     # Keep taking steps until the walk reaches the desired length.
    #     while len(self.x_values) < self.num_points:
    #         # Decide which direction to go and how far to go
    #         x_step = self.get_step()
    #         y_step = self.get_step()
    #
    #         # Reject moves that go nowhere.
    #         if x_step == 0 and y_step == 0:
    #             continue
    #
    #         # Calculate the new position.
    #         x = self.x_values[-1] + x_step
    #         y = self.y_values[-1] + y_step
    #
    #         self.x_values.append(x)
    #         self.y_values.append(y)
    #
    # def get_step(self):
    #     """calculate steps"""
    #     # Decide which direction to go and how far to go in that direction.
    #     direction = choice([1, -1])
    #     distance = choice([0, 1, 2, 3, 4])
    #     step = direction * distance
    #     return step
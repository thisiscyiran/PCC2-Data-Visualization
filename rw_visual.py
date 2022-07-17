import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Keep making new walks, as long as the progaram is active.
while True:

    rw = RandomWalk(90000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(16, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
            cmap=plt.cm.Blues, edgecolor='none', s=4)
    
    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolor='none', s=130)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
            edgecolor='none', s=130)
    
    # Remove the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)



    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break



from random import choice

def get_step():
    """ Generates step for x and y axes """
    direction = choice([1, -1])
    distance = choice([1])
    return direction * distance

x_step = get_step()
print(x_step)

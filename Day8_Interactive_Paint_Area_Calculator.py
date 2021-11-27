import math

wall_height = int(input("Please enter the height of the wall: "))
wall_width = int(input("Please enter the width of the wall: "))
coverage = 5


def paint_calc(h, w, c):
    return math.ceil((h * w) / c)


material = paint_calc(h=wall_height, w=wall_width, c=coverage)
print(
    f"You need {material} cans of paint for a wall that is {wall_height} tall and {wall_width} long. ")

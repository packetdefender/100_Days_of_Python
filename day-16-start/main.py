# import turtle
# from turtle import Turtle, Screen
#
# # Construct object from Turtle blueprint
# timmy = Turtle()
# # Change turtle shape from a carrot to a turtle
# timmy.shape("turtle")
# # Change turtle color from black to red
# timmy.color("red")
# # Move turtle forward 100 paces
# timmy.forward(100)
# # Defines screen
# my_screen = Screen()
#
# print(my_screen.canvheight)
# # This is a object method.  Instead of the screen flashing, it waits for a click event to close
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)

#from turtle import Turtle, Screen

#timmy = Turtle()


#print(timmy)
#timmy.color("green")
#timmy.shape("turtle")
#timmy.forward(100)

#my_screen = Screen()


#print(my_screen.canvheight)
#my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirel", "Charmander"])
table.add_column("Type", ["Eletrical", "Water", "Fire"])
table.align = "l"
print(table)


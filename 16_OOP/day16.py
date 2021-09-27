# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(100)

# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import  PrettyTable
mytable = PrettyTable()
mytable.title = "Pokedex"
mytable.add_column("Pokemon", ["Pikachu", "Bulbasaour", "Chalamander", "Squirtle"])
mytable.add_column("Type", ["Electric", "Grass", "Fire", "Water"])
print(mytable)
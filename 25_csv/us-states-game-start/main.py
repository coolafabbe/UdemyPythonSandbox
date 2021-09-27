import turtle
import pandas
from pandas._libs import missing

# create screen
screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()

data = pandas.read_csv("./50_states.csv")
state_names = data["state"].to_list()


game_over = False
correct_guesses = []
while not game_over:
    answer_state = screen.textinput(title=f"Guess the state {len(correct_guesses)}/50", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        pandas.DataFrame([state for state in state_names if not state in correct_guesses]).to_csv("states_to_learn.csv")
        break

    if answer_state in state_names and not answer_state in correct_guesses:
        state_data = data[data.state == answer_state]
        my_turtle.goto(int(state_data.x), int(state_data.y))
        my_turtle.write(answer_state, move=False, align="center", font=("Arial", 8, "normal"))
        correct_guesses.append(answer_state)
    
    if len(correct_guesses) == 50:
        game_over = True

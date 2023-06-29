import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
num_correct = 0
correct_guesses = []
states = pandas.read_csv("50_states.csv")

text = turtle.Turtle()
text.hideturtle()
text.penup()


while num_correct < 50:
    title = f"{num_correct}/50 States Correct"
    answer_state = screen.textinput(title=title, prompt="What's another states name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    if answer_state in states.state.values and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        num_correct += 1
        x = states[states.state == answer_state].x.values[0]
        y = states[states.state == answer_state].y.values[0]
        text.goto(x, y)
        text.write(answer_state)

df = pandas.DataFrame(columns=["States_to_Learn"])

for statey in states.state.values:
    if statey not in correct_guesses:
        df.loc[len(df.index)] = [statey]

df.to_csv("states_to_learn.csv")



from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place a bet.", prompt="Which turtle will win the race. Choose a color: ")
colors = ["red", "blue", "yellow", "green", "orange", "brown"]
all_turtles = []
y = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    all_turtles.append(new_turtle)
    y += 50

is_on = True
while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if turtle.pencolor() == user_bet:
                print(f"You've won! {turtle.pencolor()} has won the race")
            else:
                print(f"You've lost. {turtle.pencolor()} has won the race")
            is_on = False
        distance_moved = random.randint(1, 10)
        turtle.forward(distance_moved)

screen.exitonclick()

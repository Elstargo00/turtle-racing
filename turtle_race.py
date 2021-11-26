from turtle import Turtle, Screen
import random
# from random import randint

screen = Screen()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def create_turtles(colors):
    candidate_turtles = []
    turtles = [Turtle(shape="turtle") for i in range(len(colors))]
    for turtle in turtles:
        a_color = random.choices(colors)[0]
        colors.remove(a_color)
        turtle.color(a_color)
        candidate_turtles.append(turtle)
    return candidate_turtles

def setup_turtles(turtles):
    y_pos = 300
    for turtle in turtles:
        turtle.penup()
        turtle.setposition(-300, y_pos)
        y_pos -= 70

def pace_turtle(turtles):
    # check winning conditions
    for turtle in turtles:
        if turtle.pos()[0] >= 300.00:
            have_winner = True
            return (have_winner, turtle.color()[0]) # return True for have_winner
    #     pace turtle
    for turtle in turtles:
        a_pace = random.randint(0,10)
        turtle.forward(a_pace)
    return (False, "") # return False for have_winner


have_winner = False
user_bet = screen.textinput("Make your bet", "Who will win the race? Enter a colour: ")
candidate_turtles = create_turtles(colors)
setup_turtles(candidate_turtles)

while not have_winner:
    have_winner, winner = pace_turtle(candidate_turtles)

print("The turtle winner is: " + winner)
if winner == user_bet:
    print("Congratulation your turtle is the winner")
else:
    print("Too bad you lose")

screen.exitonclick()

import turtle
import random
import time
from unittest import result


wn = turtle.Screen()
wn.title("Kaplumbağ Yakalama Oyunu")
wn.bgcolor("black")
wn.setup(width=800, height=600)


score = 0
time_left = 20


score_text = turtle.Turtle()
score_text.color("white")
score_text.penup()
score_text.hideturtle()
score_text.goto(0, 260)
score_text.write("Puan: {}".format(score), align="center", font=("Courier", 24, "normal"))


countdown_text = turtle.Turtle()
countdown_text.color("white")
countdown_text.penup()
countdown_text.hideturtle()
countdown_text.goto(0, -280)
countdown_text.write("Kalan Süre: {}".format(time_left), align="center", font=("Courier", 24, "normal"))


target = turtle.Turtle()
target.shape("turtle")
target.color("green")
target.penup()
target.shapesize(stretch_wid=3, stretch_len=3)


def relocate_object():
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    target.goto(x, y)


def toggle_visibility():
    target.hideturtle()
    relocate_object()
    target.showturtle()
    wn.ontimer(toggle_visibility, 1000)


def catch(x, y):
    global score
    if target.distance(x, y) < 20:  # Eğer tıklanan nokta hedefin içindeyse puanı artır
        score += 1
        score_text.clear()
        score_text.write("Puan: {}".format(score), align="center", font=("Courier", 24, "normal"))


target.onclick(catch)


def countdown():
    global time_left
    time_left -= 1
    countdown_text.clear()
    countdown_text.write("Kalan Süre: {}".format(time_left), align="center", font=("Courier", 24, "normal"))


    if time_left == 0:
        wn.clear()
        if score >= 15:
            result_text = "! WINNER:))"
        else:
            result_text = "! GAME OVER:("
        result = turtle.Turtle()
        result.color("red")
        result.penup()
        result.hideturtle()
        result.goto(0, 0)
        result.write(result_text, align="center", font=("Courier", 36, "normal"))
        restart_text = turtle.Turtle()
        restart_text.color("black")
        restart_text.penup()
        restart_text.hideturtle()
        restart_text.goto(0, -50)
        restart_text.write("SPACE tuşuna basarak yeniden oynayabilirsiniz", align="center",
                           font=("Courier", 18, "normal"))
        wn.onkey(restart_game, "space")
        return


    wn.ontimer(countdown, 500)


def restart_game(restart_text=None):
    global score, time_left
    score = 0
    time_left = 20
    score_text.clear()
    score_text.write("Puan: {}".format(score), align="center", font=("Courier", 24, "normal"))
    countdown_text.clear()
    countdown_text.write("Kalan Süre: {}".format(time_left), align="center", font=("Courier", 24, "normal"))
    result.clear()
    restart_text.clear()
    relocate_object()
    target.showturtle()
    wn.ontimer(countdown, 1000)


wn.ontimer(countdown, 1000)


relocate_object()
target.showturtle()


wn.ontimer(toggle_visibility, 100)

wn.listen()
wn.mainloop()

import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.end_fill()
    turtle.pendown()

dolu = turtle.Turtle()
dolu.shape("turtle")
dolu.speed(1)

draw_circle(dolu, "green", 50, 25, 0)
draw_circle(dolu, "blue", 50, 0, 0)
draw_circle(dolu, "yellow", 50, -25, 0)

dolu.penup()
dolu.goto(0, -50)
dolu.color('black')
dolu.write("Let's Learn Python!", align="center", font=(None, 16, "bold"))
dolu.goto(0, -80)
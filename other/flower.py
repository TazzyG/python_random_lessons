import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(0,3):
        some_turtle.forward(50)
        some_turtle.right(120)       

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(3)
    for i in range(1,37):
        draw_triangle(brad)
        brad.right(10)
draw_art()

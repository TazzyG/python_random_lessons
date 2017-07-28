import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(0,3):
        bernie.forward(50)
        bernie.right(120)       

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(3)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #Create the turtle Angie - Draws a circle
    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("pink")
    # angie.circle(100)
    #Create the turtle Bernie - Draws a triangle
    # bernie = turtle.Turtle()
    # bernie.shape("triangle")
    # bernie.color("red")
    # draw_triangle(bernie)    window.exitonclick()

draw_art()


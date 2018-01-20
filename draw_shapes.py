import turtle

def draw_square(some_turtle):
    #Creating a Square
    for vertices in range (0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle():
    # Creating a second turtle
    josercleia = turtle.Turtle()
    josercleia.shape("turtle")
    josercleia.color("#EF767A")
    josercleia.circle(100)

def draw_triangle():
    clarisvaldo = turtle.Turtle()
    clarisvaldo.shape("turtle")
    clarisvaldo.color("#F79F79")
    for vertices in range (0,3):
        clarisvaldo.right(120)
        clarisvaldo.forward(60)


#Calling functions together
def runway():
    #Creating a runway
    runway = turtle.Screen()
    runway.bgcolor("#21897E")

    # Creating a new turtle called Jobervaldo. I already love him <3
    jobervaldo = turtle.Turtle()
    jobervaldo.shape("turtle")
    jobervaldo.color("#FFCE60")
    jobervaldo.speed(5)

    for squares in range(0, 36):
        draw_square(jobervaldo)
        jobervaldo.right(10)

    runway.exitonclick()

runway()


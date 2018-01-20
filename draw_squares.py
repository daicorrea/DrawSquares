import turtle

def draw_square():
    #Creating a new turtle called Jobervaldo. I already love him <3
    jobervaldo = turtle.Turtle()
    jobervaldo.shape("turtle")
    jobervaldo.color("#FFCE60")
    jobervaldo.speed(1)

    #Creating a Square
    for vertices in range (0,4):
        jobervaldo.forward(100)
        jobervaldo.right(90)

def draw_circle():
    # Creating a second turtle
    josercleia = turtle.Turtle()
    josercleia.shape("turtle")
    josercleia.color("#EF767A")
    josercleia.circle(100)

#Calling functions together
def runway():
    #Creating a runway
    runway = turtle.Screen()
    runway.bgcolor("#21897E")

    draw_square()
    draw_circle()

    runway.exitonclick()

runway()


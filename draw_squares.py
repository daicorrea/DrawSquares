import turtle

def draw_square():
    #Creating a new turtle called Jobervaldo. I already love him <3
    jobervaldo = turtle.Turtle()
    jobervaldo.shape("turtle")
    jobervaldo.color("#FFCE60")
    jobervaldo.speed(1)
    #Creating a runway for Jobervalto to parede
    runway = turtle.Screen()
    runway.bgcolor("#21897E")

    #Print has to be separated because it's not possible to concatenate the string with a Vec2D object
    print("Jobervaldo started walking in the position: ")
    print(jobervaldo.position())
    #Creating a Square
    for vertices in range (0,4):
        jobervaldo.forward(100)
        jobervaldo.right(90)
        print("Jobervaldo is now in the position: ")
        print(jobervaldo.position())

    #Creating a second turtle
    josercleia = turtle.Turtle()
    josercleia.shape("turtle")
    josercleia.color("#EF767A")
    josercleia.circle(100)

    runway.exitonclick()

draw_square()

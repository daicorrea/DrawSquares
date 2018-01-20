import turtle

def draw_square():
    #Creating a new turtle called Jobervaldo. I already love him <3
    jobervaldo = turtle.Turtle()
    #Creating a runway for Jobervalto to parede
    runway = turtle.Screen()
    runway.bgcolor("red")

    #Print has to be separated because it's not possible to concatenate the string with a Vec2D object
    print("Jobervaldo started walking in the position: ")
    print(jobervaldo.position())
    #Creating a Square
    for vertices in range (0,4):
        jobervaldo.forward(100)
        jobervaldo.right(90)
        print("Jobervaldo is now in the position: ")
        print(jobervaldo.position())

    runway.exitonclick()

draw_square()

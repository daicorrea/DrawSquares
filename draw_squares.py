import turtle

def draw_square():
    #Creating a new turtle called Jobervaldo. I already love him <3
    jobervaldo = turtle.Turtle()
    #Print has to be separated because it's not possible to concatenate the string with a Vec2D object
    print("Jobervaldo started walking in the position: ")
    print(jobervaldo.position())
    #Starting Walking in pixels
    jobervaldo.forward(100)
    print("Jobervaldo is now in the position: ")
    print(jobervaldo.position())

draw_square()

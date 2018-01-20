import turtle

def draw_square():
    #Creating a new turtle called Jobervaldo. I already love him <3
    jobervaldo = turtle.Turtle()
    position = jobervaldo.position()
    #Print has to be separated because it's not possible to concatenate the string with a Vec2D object
    print("Jobervaldo started walking in the position: ")
    print(position)

draw_square()

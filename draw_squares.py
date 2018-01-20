import turtle

def draw_square():
    position = turtle.position()
    #print has to be separated because it's not possible to concatenate the string with a Vec2D object
    print("Initial position is: ")
    print(position)

draw_square()

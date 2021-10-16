import turtle

while True:  # https://www.includehelp.com/python/asking-the-user-for-integer-input-in-python-limit-the-user-to-input-only-integer-value.aspx
    try:
        sides = int(input("How many sides?: "))  # get # of sides
        break
    except ValueError:  # If not integer
        print("Integers Only")
        continue

while True:
    try:
        color = input('Enter a color: ') # Get color
        turtle.fillcolor(color)
        break
    except turtle.TurtleGraphicsError:   # If not valid
        print('Not a valid color')
        continue


angle = 180-(((sides - 2) * 180)/sides)     # Calculating angle


turtle.speed(1) # Turtle Settings
turtle.hideturtle()


turtle.begin_fill() # Start fill
for i in range(0,sides):        # Drawing polygon
    turtle.forward(50)          # Drawing polygon
    turtle.right(angle)         # Drawing polygon

turtle.end_fill()   #End fill


input('Press enter to exit')

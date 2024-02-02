import turtle
import random

# Function to draw a square with a random color
def draw_square(size):
    turtle.color(random.choice(colors))  # Randomly choose a color from the list
    turtle.begin_fill()  # Begin filling the square
    for _ in range(4):
        turtle.forward(size)  # Draw each side of the square
        turtle.left(90)
    turtle.end_fill()  # End filling the square

# Set up the turtle screen
turtle.speed(0)
turtle.hideturtle()
turtle.title("Random Squares")

# Define a list of colors
colors = ["red", "yellow", "green", "blue"]

# Ask the user for the number of squares to draw
num_squares = int(turtle.numinput("Number of Squares", "Enter the number of squares to draw:", default=5, minval=1))

# Draw the specified number of squares at random locations
for _ in range(num_squares):
    size = random.randint(20, 20)  # Random size for each square
    x_pos = random.randint(-200, 200)  # Random x-coordinate
    y_pos = random.randint(-200, 200)  # Random y-coordinate

    turtle.penup()  # Lift the pen to move without drawing
    turtle.goto(x_pos, y_pos)  # Move to the random position
    turtle.pendown()  # Lower the pen to start drawing

    draw_square(size)  # Call the function to draw a square with random color

# Display the result until the user clicks on the window
turtle.done()

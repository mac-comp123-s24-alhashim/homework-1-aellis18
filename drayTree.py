import turtle

# Function to draw a tall brown rectangle with green circles around the top
def draw_tree(trunk_height, trunk_width, circle_radius, num_circles):
    # Set trunk color
    turtle.color("saddlebrown")
    turtle.begin_fill()

    # Draw trunk
    for _ in range(2):
        turtle.forward(trunk_width)
        turtle.left(90)
        turtle.forward(trunk_height)
        turtle.left(90)

    turtle.end_fill()

    # Move to the top of the trunk
    turtle.left(90)
    turtle.forward(trunk_height)
    turtle.right(90)

    # Set circle color
    circle_color = "forest green"
    turtle.color(circle_color)

    # Draw little green circles around the top
    turtle.penup()
    turtle.goto(turtle.xcor() - circle_radius * num_circles, turtle.ycor())
    turtle.pendown()

    for _ in range(num_circles):
        turtle.begin_fill()
        turtle.circle(circle_radius)
        turtle.end_fill()

        # Move to the starting position for the next circle
        turtle.penup()
        turtle.forward(circle_radius * 2)
        turtle.pendown()

# Set up the turtle screen
turtle.speed(2)
turtle.hideturtle()
turtle.title("Tall Tree with Green Circles")

# Set background color
turtle.bgcolor("skyblue")

# Move to the starting position
turtle.penup()
turtle.goto(-50, -150)
turtle.pendown()

# Draw a tall brown rectangle with green circles around the top
draw_tree(120, 20, 8, 10)

# Hide the turtle and display the result
turtle.hideturtle()
turtle.done()


# Draws six circles, centered on the origin, each a different color.
# Assumption: the number of colors in the turtle colors list is at least
# as long as the number of rings.

import turtle


scr = turtle.Screen()
turtle = turtle.Turtle()

scr.bgcolor("seashell")

tColors = ["light salmon", "light sky blue", "pale green", "light coral", "pale turquoise", "plum"]

turtle.width(5)
numRings = 6

for i in range(numRings):
    turtle.color(tColors[i])  # Bug: The script incorrectly used tColors[0] for all circles. Changed to tColors[i].
    radius = 40 * (i + 1)

    turtle.up()
    turtle.forward(radius)
    turtle.down()

    turtle.left(90)
    turtle.circle(radius)  # Bug: The script used 'i' instead of 'radius' for circle radius. Changed to 'radius'.
    turtle.right(60)

    turtle.up()  # Bug: The script used 'turtle.up' without parentheses. Changed to 'turtle.up()'.
    turtle.backward(radius)
    turtle.down()

scr.exitonclick()

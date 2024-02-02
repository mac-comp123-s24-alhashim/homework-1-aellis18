# Autonomous Search-and-Rescue Drone Script
# This script calculates the center point, the radius of the largest circle needed to cover a given rectangular search area,
# and the number of circles the drone needs to fly in a circular search pattern.
# The search pattern ensures each circle has a radius 5 meters larger than the previous one.
# Author: Your Name

# Import the math module
import math

# Ask the user for the width and height of the search area
width = float(input("Enter the width of the search area (in meters): "))  # User input for the width of the search area
height = float(input("Enter the height of the search area (in meters): "))  # User input for the height of the search area

# Compute and output the center point
center_x = width / 2  # Calculate the x-coordinate of the center point
center_y = height / 2  # Calculate the y-coordinate of the center point
print(f"Center point for the search area: ({center_x:.2f}, {center_y:.2f})")  # Output the center point coordinates

# Compute the radius of the largest circle
diagonal = math.sqrt(width**2 + height**2)  # Calculate the diagonal of the search area using Pythagorean theorem
radius_largest_circle = diagonal / 2  # Calculate the radius of the largest circle
print(f"Radius of the largest circle needed: {radius_largest_circle:.2f} meters")  # Output the radius of the largest circle

# Calculate the number of circles needed
circles_needed = math.ceil(radius_largest_circle / 5)  # Round up to the nearest integer for the number of circles needed
print(f"Number of circles the drone needs to fly: {circles_needed}")  # Output the number of circles needed

# Optional: Output diameters of each circle
for i in range(1, circles_needed + 1):  # Loop through the range of circles needed
    circle_radius = 5 * i  # Calculate the radius of the current circle
    circle_diameter = 2 * circle_radius  # Calculate the diameter of the current circle
    print(f"Circle {i}: Diameter = {circle_diameter:.2f} meters")  # Output the diameter of the current circle







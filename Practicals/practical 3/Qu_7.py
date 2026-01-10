#  Write a program to calculate surface volume and area of a cylinder.

Pi = 3.14

# Reading radius and height of cylinder
radius = float(input("Enter radius of cylinder(cm): "))
height = float(input("Enter height of cylinder(cm): "))

# Calculating the area and volume of cylinder
Curved_area = 2 * Pi * radius * height
Total_area = 2 * Pi * radius * (radius + height)
Volume = Pi * radius * radius * height

# Displaying the results
print(f"Curved Area of Cylinder is: {Curved_area:.4f}")
print(f"Total Area of Cylinder is: {Total_area:.4f}")
print(f"Volume of the Cylinder is: {Volume:.4f}")
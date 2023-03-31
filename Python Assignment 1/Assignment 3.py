#enter the input from the user
radius = float(input("Enter the radius of the circle: "))

#calculations
pi = 3.14
area = pi * radius ** 2
circumference = 2 * pi * radius

#print the area and circumference of a circle
print(f"The area of the circle is {area:.2f}")
print(f"The circumference of the circle is {circumference:.2f}")

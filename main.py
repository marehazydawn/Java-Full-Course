import math

radius = float(input('enter the radius of a circle: '))

# circumference = 2 * math.pi * radius
# print(f"The circumference is: {round(circumference, 2)} cm")

area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}cm^2")
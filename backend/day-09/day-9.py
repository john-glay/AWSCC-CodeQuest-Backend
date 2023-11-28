import circle

radius = int(input("\nInput radius: "))

diameter = circle.calculate_diameter(radius)
circumference = circle.calculate_circumference(radius)
area = circle.calculate_area(radius)

print(f"\nGiven radius: {radius}")
print(f"Diameter: {diameter}")
print(f"Circumference: {circumference}")
print(f"Area: {area}\n")
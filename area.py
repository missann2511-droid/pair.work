
print("Choose a shape to calculate area:")
print("1 - Square")
print("2 - Circle")
print("3 - Rectangle")
print("4 - Triangle")

choice = input("Enter the number of the shape: ")

if choice == "1":
    a = float(input("Enter the length of the square's side: "))
    area = a * a
    print("Area of the square:", area)
elif choice == "2":
    r = float(input("Enter the radius of the circle: "))
    area = 3.14 * r * r
    print("Area of the circle:", area)
elif choice == "3":
    a = float(input("Enter the length of the rectangle: "))
    b = float(input("Enter the width of the rectangle: "))
    area = a * b
    print("Area of the rectangle:", area)
elif choice == "4":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = (base * height) / 2
    print("Area of the triangle:", area)

else:

   print("Incorect: Valid shapes choices are 1,2,3,4")


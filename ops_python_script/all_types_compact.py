
#trying to campact all together.
#integer
age = int(input("Enter your age: "))

#float
height = float(input("Enter your height in meters: "))

#string
name = "Alice"

#boolean
is_student = True

#list
scores = [80, 90, 75, 88]

# Tuple
dimensions = (5.5, 3.2)

# Dictionary
person = {"name": name, "age": age}
# Set
unique_numbers = {1, 2, 3, 2, 1}
#some calculations
average_score = sum(scores) / len(scores)
area = dimensions[0] * dimensions[1]
bmi = (age / height ** 2)


#printing  out 
print("Name: {name}")
print("Age: {age}")
print("Height: {height} m")
print("Is student: {is_student}")
print("Average Score: {average_score}")
print(f"Rectangle Area: {area}")
print(f"Person Dictionary: {person}")


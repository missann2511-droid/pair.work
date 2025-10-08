# List example
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange') 
print('List:', fruits) 

# Tuple example
coordinates = (100, 20)
print('Tuple:', coordinates)

# Dictionary example
student = {'name': 'Sergey', 'age': 21, 'courses': ['Management', 'Analytics']}
print('Dictionary:', student)
student['age'] = 22  
print('Updated age:', student['age'])

# Nested dictionary with list
school = {
    'name': 'GSOM',
    'departments': {
        'Math': ['Algebra', 'Analysis'],
        'CS': ['Programming', 'AI']
    }
}
print('Nested dict:', school)

# Set example
numbers = {1, 2, 3, 2, 1}
print('Set:', numbers)  # duplicates removed
numbers.add(4)
print('Set after add:', numbers)

# Checking membership
print('Is 3 in numbers?', 3 in numbers)
print('Is orange in fruits?', 'orange' in fruits)


x = 15          
pi = 3.14159    

num_str = input("Введите число: ")  
num = int(num_str)                   

sum_result = x + num
mul_result = pi * num
power_result = x ** 2

sum_str = str(sum_result)
mul_str = f"{mul_result:.2f}"  

print(f"Сумма: {sum_result}")
print(f"Произведение: {mul_result}")
print(f"Квадрат x: {power_result}")
print(f"Сумма как строка: '{sum_str}'")
print(f"Произведение форматированное: {mul_str}")

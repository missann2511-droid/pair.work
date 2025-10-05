age = int(input("Введите ваш возраст: "))

if age >= 18:
    print("Вы совершеннолетний.")
else:
    print("Вы несовершеннолетний.")

is_member = age >= 65
print(f"Пенсионер: {is_member}")
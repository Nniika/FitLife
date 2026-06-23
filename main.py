print("Привет! Я фитнес-бот!")
print("Давай познакомимся!")

user_name = input("Как тебя зовут? ")
while True:
    try:
        user_age = int(input("Сколько тебе лет? "))
        break
    except ValueError:
        print("Ошибка! Введите число, например: 25")

while True:
    try:
        user_weight = float(input("Какой у тебя вес (в кг)? Используй точку, например: 75.5 "))
        break
    except ValueError:
        print("Ошибка! Введите число с точкой, например: 75.5")

while True:
    try:
        user_height = float(input("Какой у тебя рост (в метрах)? Используй точку, например: 1.75 "))
        break
    except ValueError:
        print("Ошибка! Введите число с точкой, например: 1.75") # Я написала с помощью ИИ, я еще очень плохо понимаю куда что применять надо((

bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)

water_ml = user_weight * 30
water_l = round(water_ml / 1000, 2)

print("\n" + "=" * 40)
print("    РЕЗУЛЬТАТЫ РАСЧЕТА")
print("=" * 40)
print(f"Имя: {user_name}")
print(f"Возраст: {user_age} лет")
print(f"ИМТ: {bmi_rounded}")
print(f"Норма воды: {water_l} литра в день")
print("=" * 40)
print("Расчет окончен. Будьте здоровы!")

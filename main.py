print("Привет! Я фитнес-бот!")
print("Давай познакомимся!")

user_name = input("Как тебя зовут? ")
user_age = int(input("Сколько тебе лет? "))

user_wieght = float(input("Какой у тетя вес (в кг)? "))
user_height = float(input("Какой у тебя рост (в метрах)? Например, 1.75: "))

bmi = user_wieght / (user_height ** 2)
bmi_rounded = round(bmi, 1)

water_ml = user_wieght * 30
water_1 = water_ml / 1000

print("\n" + "=" * 40)
print("        РЕЗУЛЬТАТЫ РАСЧЕТА")
print("=" * 40)
print(f"Имя: {user_name}")
print(f"Возраст: {user_age} лет")
print(f"ИМТ: {bmi_rounded}")
print(f"Норма воды: {water_1} литра в день")
print("=" *40)
print("Расчет окончен. Будьте здоровы!")


#мне помог ИИ, тк я еще прям очень сильно теряюсь без подсказок 

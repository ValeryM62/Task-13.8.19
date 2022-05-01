try:
    n = int(input("количество билетов: "))
    print("Укажите возраст каждого посетителя")
    s = 0
    for i in range(n):
        age = int(input("Возраст: "))
        if age < 18:
            s += 0
        elif 18 <= age <25:
            s += 990
        else:
            s += 1390
    if n > 3:
        f = 0.9
    else:
        f = 1
except ValueError as e:
    print("некорректный ввод")
else:
    print("С вас -", s * f, "рублей" )



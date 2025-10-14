print("{:^35}".format("=== ЖУРНАЛ ОЦЕНОК ==="))
print("{}".format("\n🎓 Проект: Учёт оценок студентов"))
print("{}".format("📋 Описание:"))
print("{}".format("Программа позволяет добавлять студентов и их оценки,"))
print("{}".format("считать средний балл каждого, находить лучшего и худшего ученика,"))
print("{}".format("а также вычислять общий средний балл группы."))

student = [
    ["Alex", 5, 8, 10],
    ["Diana", 7, 9, 11],
    ["Oleg", 3, 4, 6]
]

while True:
    print("\n{:^35}".format("=== Список учеников ==="))
    print("\n{:<17} {:<5} {:<5} {:<5}".format("Имя ученика", "МАТАН", "АНГЛ", "ФИЗРА"))
    for row in range(len(student)):
        name = student[row][0]
        matan = student[row][1]
        angl = student[row][2]
        phys = student[row][3]
        print(f"\n{row + 1}. {name:<15} {matan:<5} {angl:<5} {phys}")
    print("\n - Добавление ученика - 1")
    print(" - Средний бал ученика - 2")
    print(" - Лучший ученик - 3")
    print(" - Общий средний балл - 4")

    choice = input("\nВведите команду -> ")

    if choice == "1":
        new_name = input("Введите имя ученика -> ")
        new_matan = int(input("Введите оценку по математике -> "))
        new_angl = int(input("Введите оценку по английскому -> "))
        new_phys = int(input("Введите оценку по физкультуре -> "))
        new_list = [new_name, new_matan, new_angl, new_phys]
        student.append(new_list)
    elif choice == "2":
        name_number = int(input("Введите номер ученика -> "))
        avarage = int((sum(student[name_number - 1][1:4]))) / len(student[name_number - 1][1:4])
        print(f"\nСредний бал ученика {student[name_number - 1][0]} - {avarage:.2f}!")
        back = input("\nЧтобы вернутся назад введите 0 -> ")
        if back == "0":
            continue
    elif choice == "3":
        new_list_avarage = []
        for row in student:
            new_list_avarage.append(float(sum(row[0:][1:]) / len(row[0:][1:])))
        max_index = new_list_avarage.index(max(new_list_avarage))
        print(f"\nЛучший ученик {student[max_index][0]} со средним балом {new_list_avarage[max_index]}!")
        back = input("\nЧтобы вернутся назад введите 0 -> ")
        if back == "0":
            continue
    elif choice == "4":
        new_list_avarage = []
        for row in student:
            new_list_avarage.append(float(sum(row[0:][1:]) / len(row[0:][1:])))
        summ_avarage = sum(new_list_avarage) / len(new_list_avarage)
        print(f"\nОбщий средний бал учеников - {summ_avarage:.2f}!")
        back = input("\nЧтобы вернутся назад введите 0 -> ")
        if back == "0":
            continue

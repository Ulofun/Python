from failing import saving_data as fsd
from failing import teacher_school as fts


def teacher_get():
    searchname = input("Введите фамилию для поиска ученика: ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    stfile = open(fsd.studentfailing, "r+", encoding='utf-8')
    filecontents = stfile.readlines()

    info1 = False
    for ifline in filecontents:
        if searchname in ifline:
            print(f"\nПо вашему запросу найдена фамилия ученика {ifline}")
            print("Выберите вариант действий: ")
            print("1. Поставить оценку ученику.")
            print("2. Вернуться к поиску ученика.")
            print('3. Вернуться к "Меню учителя".')
            var = int(input("Введите выбранный вариант: "))
            if var == 1:
                linename = ifline[0:len(ifline)-1]
                vhis = int(input("Введите сколько предметов ученик сдал: "))
                for _ in range(vhis):
                    detals = str(input("Введите название проведённого предмета: "))
                    get = int(input("Введите оценку: "))
                    detalsget = f" |{detals} {get}| "
                    linename = linename + detalsget
                summlinename = linename

                myfile = open(fsd.schoolfailing, "a+", encoding='utf-8')
                myfile.writelines(f"{summlinename}\n")
                print(f"Оценки ученика {linename} успешно добавлены в список!")
                myfile.close

            elif var == 2:
                print("Вы выбрали 2 вариант и вернётесь к выбору ученика!")
                teacher_get()
            elif var == 3:
                print('Вы выбрали 3 вариант и вернётесь в "Меню учителя"')
                fts.teachet_menu()
            else:
                print(f"Такого варианта нет!")
                teacher_get()

            info1 = True
            break
    if info1 == False:
        print(f"Фамилия {searchname} в списке учеников не найдена!")






def student_get():
    print()
    searchname = input("Введите фамилию для поиска ученика: ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    myfile = open(fsd.schoolfailing, "r+", encoding='utf-8')
    fileinfo = myfile.readlines()

    info2 = False
    for line in fileinfo:
        if searchname in line:
            print("\nПо вашему запросу найдена фамилия ученика!")
            print(f"Данные ученика: \n{line}")
            info2 = True
            break
    if info2 == False:
        print(f"Фамилия {searchname} в дневнике учеников не найдена!")


def data_get():
    print("\nВы решили обновить дневник учеников.\n")
    print("Введите дату: день|месяц|год для обновления.\n")
    day = int(input("Введите день: "))
    month = input("Введите месяц: ")
    year = int(input("Введите год: "))
    myfile = open(fsd.schoolfailing, "w", encoding='utf-8')
    myfile.writelines(f"{day} | {month} | {year}\n")
    myfile.close
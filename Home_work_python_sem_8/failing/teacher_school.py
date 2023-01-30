from failing import school_menu as fsm
from failing import saving_data as fsd
from failing import input_model as fim
from failing import get

def teachet_menu():
    print("\nВы перешли в меню учителя!\n")
    print("Выберите один из вариантов:")
    print("1. Вывести список учеников.")
    print("2. Ввести нового ученика в список.")
    print("3. Обновить дневник учеников")
    print("4. Поставить оценку ученику.")
    print("5. Возврат на главное меню.\n")
    men = int(input("Введите цифру выбранного варианта: "))
    if men == 1:
        stfile = open(fsd.studentfailing, "r+", encoding='utf-8')
        filestudent = stfile.read()
        if len(filestudent) == 0:
            print("\nИскомый контакт не обнаружен, сожалею.\n")
        else:
            print("\nВот список учеников:\n")
            print(filestudent)
        stfile.close
        enter = input("Для продолжения нажмите Enter")
        teachet_menu()
    elif men == 2:
        fim.input_student()
        enter = input("Для продолжения нажмите Enter")
        teachet_menu()
    elif men == 3:
        get.data_get()
        enter = input("Для продолжения нажмите Enter")
        teachet_menu()
    elif men == 4:
        get.teacher_get()
        enter = input("Для продолжения нажмите Enter")
        teachet_menu()
    elif men == 5:
        print('Вы выбрали 4 вариант и вернётесь в "Школьное меню".')
        fsm.school_menu()
    else:
        print("Вы ввели неправильный вариант, повторите выбор!")
        teachet_menu()
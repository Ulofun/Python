from failing import school_menu as fsm
from failing import saving_data as fsd
from failing import get

def student_menu():
    print("\nВы перешли в меню ученика!\n")
    print("Выберите один из вариантов:")
    print("1. Вывести список учеников.")
    print("2. Просмотреть информацию об ученике.")
    print("3. Возврат на главное меню.\n")
    ren = int(input("Введите цифру выбранного варианта: "))
    if ren == 1:
        stfile = open(fsd.studentfailing, "r+", encoding='utf-8')
        filestudent = stfile.read()
        if len(filestudent) == 0:
            print("\nИскомый контакт не обнаружен, сожалею.\n")
        else:
            print("\nВот список учеников:\n")
            print(filestudent)
        stfile.close
        enter = input("Для продолжения нажмите Enter")
        student_menu()
    elif ren == 2:
        get.student_get()
        enter = input("Для продолжения нажмите Enter")
        student_menu()
    elif ren == 3:
        print('\nВы выбрали 3 вариант и вернётесь в "Школьное меню".\n')
        fsm.school_menu()
    else:
        print("\nВы ввели неправильный вариант, повторите выбор!\n")
        student_menu()
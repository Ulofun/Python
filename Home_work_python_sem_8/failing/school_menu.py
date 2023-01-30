from failing import teacher_school as fts
from failing import student_school as fss


print("\nШкольное меню!\n")

def school_menu():
    print("Пользователь должен укзать свой стаус для продолжения!")
    print('"Ученик" || "Учитель"')
    status = str(input("Укажите вашь статус: "))
    if status.lower() == "ученик":
        fss.student_menu()
    elif status.lower() == "учитель":
        fts.teachet_menu()
    else:
        print("Вы ввели неправильный статус.")
        print("Повторите ввод.")
        enter = input("Для продолжения нажмите Enter")
        school_menu()
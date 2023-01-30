from failing import saving_data as fsd

def input_firstname():
    first = input("Введите имя ученика: ")
    remfname = first[1:]
    firstchar = first[0]
    return firstchar.upper() + remfname

def input_lastname():
    last = input("Введите фамилию ученика: ")
    remlname = last[1:]
    firstchar = last[0]
    return firstchar.upper() + remlname

def input_student():
    print("Введите нового ученика в список.")
    firstname = input_firstname()
    lastname = input_lastname()
    contactDetails = (f"{firstname} {lastname}\n")

    stfile = open(fsd.studentfailing, "a", encoding='utf-8')
    stfile.write(contactDetails)
    stfile.close
    print(f"Новый ученик:\n\n{contactDetails}\nуспешно добавлен в список!")
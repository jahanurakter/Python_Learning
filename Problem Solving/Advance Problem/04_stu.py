s_DB = []

def add():
    s_id = input("Enter your id:"),
    s_name = input("Enter your name:"),
    s_age = int(input("Enter your age:"))
    s_roll = input("Enter your roll:"),
    s_clas = input("Enter your clas:"),

    add_s= {
        "s_id": s_id,
        "s_name": s_name,
        "s_age": s_age,
        "s_roll": s_roll,
        "s_clas": s_clas,
        "s_total": s_id
    }

    s_DB.append(add_s)
    print("Successfully added")

def view():
    for x in s_DB:
        print(x)

def total_stu():
     print(f"Total Student Count: {len(s_DB)}")


def replace():
    search_id=input("Enput student ID:")

    for x in s_DB:
        if x [s_DB] == search_id:

            x['s_name'] = input("Enter your new name:")
            x["s_age"] = int(input("Enter yout new age:"))

        else:
            print("Your ID not found")
while True:
    print(''' 
            Press 1 for Add
            Press 2 for View
            Press 3 for Replace
            Press 4 for total Student
            Press 5 for Exit
    ''')
    value = input("Enter Your Choice:")
    if value == "1" :
        add()
    elif value == "2":
        view()
    elif value == "3":
        replace()
    elif value == "4":
        total_stu()
    elif value == "5":
        break



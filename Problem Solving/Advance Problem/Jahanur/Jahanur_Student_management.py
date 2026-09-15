
stu_db = []

def add_stu():
    s_id = input("Enter your id: ")
    s_name = input("Enter your name: ")
    s_age = int(input("Enter your age: "))
    s_dept = input("Enter your dept: ")
    s_marks = float(input("Enter your marks: "))

    if 80<=s_marks<=100:
        s_grade = "1st Div"
    elif 60<=s_marks<=79:
        s_grade = "2nd Div"
    elif 40<=s_marks<=59:
        s_grade = "3rd Div"
    elif 0<=s_marks<=39:
        s_grade = "Fail"
    else:
        print("Input Valid Marks""\n"'Marks must be 0-100')

        return

    stu ={
        "s_id": s_id ,
        "s_name": s_name ,
        "s_age": s_age,
        "s_dept": s_dept,
        "s_marks": s_marks,
        "s_grade": s_grade
        }
    stu_db.append(stu)
    print("Student Added Succesfully")

def view_stu():
    
    if len(stu_db) == 0 :
        print("Student not found")
    print("Total student:", len(stu_db))

    for student in stu_db:
        print(student)
    
def search_stu():
    if len(stu_db) == 0:
        print("Student not available")
        return
    search = input("Enter Id or Name for search: ")
    for x in stu_db:
     if x["s_id"] == search or x["s_name"].lower() == search.lower():
         print(x)
         return
    print("Student not found")
    return

def update_stu():
    if len(stu_db) == 0:
            print("Student not available")
            return
    search = input("Enter Id for update: ")
    for x in stu_db:
         if x["s_id"] == search :

            x["s_name"] = input("Enter new name: ")
            x["s_age"] = int(input("Enter new age: "))
            x["s_dept"] = input("Enter new department: ")

            new_marks = float(input("Enter new marks: "))

            if 80<=new_marks<=100:
                x ["s_grade"] = "1st Div"
            elif 60<=new_marks<=79:
                x ["s_grade"] = "2nd Div"
            elif 40<=new_marks<=59:
                x ["s_grade"] = "3rd Div"
            elif 0<=new_marks<=39:
                x ["s_grade"] = "Fail"
            else:
                    print("Input Valid Marks""\n"'Marks must be 0-100')
                    return

            x ["s_marks"] = new_marks

            print("Student Updated Successfully")
            return
    print("Student not found")

def del_stu():
    if len(stu_db) == 0:
            print("Student not available")
            return
    search = input("Enter Id for Delete: ")
    for stu in stu_db:
        if stu["s_id"] == search:
            stu_db.remove(stu)
            print("Student Remove Succesfully")
            return

while True:
    print('''
        1. For Add
        2. For View
        3. For Search
        4. For Update
        5. For Delete
        6. Exit
        ''')

    option = input("Enter option between 1 to 6: ")

    if option == "1":
        add_stu()
    elif option == "2":
        view_stu()
    elif option == "3":
        search_stu()
    elif option == "4":
        update_stu()
    elif option == "5":
        del_stu()
    elif option == "6":
        break
    else:
        print("Input Valid Option.")


    

     
     
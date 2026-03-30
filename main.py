from student import *
from file import*

student= []

cont =1
while cont ==1:
    
    #menu
    try:
        print("\nSystem  Menu\n")
        opcion = int(input("1-add student .\n"
                        "2-search students.\n"
                        "3-search student for ID.\n"
                        "4-update information the student.\n"
                        "5-Delete.\n"
                        "6-save CSV.\n"
                        "7-laod CSV.\n"
                        "8-Exit.\n"
                        "Enter number (1-6): "))
        # add
        if opcion == 1:
            add = new_student()
            student.append(add)
            continue
        
        # search
        elif opcion == 2:
            summary(student)
            continue
        
        # ID
        elif opcion == 3:
            search_student_ID(student)
            continue
        
        # update
        elif opcion == 4:
            update_student(student)
            continue
        
        # Delete
        elif opcion == 5:
            Delete_student(student)
            continue
        
        # save CSV
        elif opcion == 6:
            name_CSV = validation_str("Enter name file")
            name_CSV += ".csv"
            save_csv(student, name_CSV)
            continue
        
        # laod CSV
        elif opcion == 7:
            name_CSV = validation_str("Enter name file")
            name_CSV += ".csv"
            csv_1 = load_csv(name_CSV)
            
            if csv_1:
                opcion = input("¿inventary (yes/no): ").upper()

                if opcion == "YES":
                    student = csv_1
                    print("\n new inventary\n")

                elif opcion == "NO":
                    
                    for new in csv_1:
                        value = False

                        for actual in student:
                            if actual["ID"] == new["ID"]:
                                actual["name"] = new["name"]
                                actual["age"] = new["age"]
                                actual["program"] = actual["program"]
                                actual["stade"] = new["stade"]
          
                                value = True
                                break

                        if not value:
                            student.append(new)

                    print("\n NEW inventary\n")

            continue
        
        # Exit
        elif opcion == 8:
            print("Exit the System...........")
            cont =2
        else:
            print("You must enter a valid value (1-8)")
            
    except ValueError:
        print("the value must be numeric (1-8)")
        continue
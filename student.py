from validation import *

# add student
def new_student(stade=True):
    print("\nNew student\n")
    valueID = validation_int("Add ID student ") 
    name = validation_str("Add name student ")
    age = validation_int("Add age student ")
    program =  validation_str("Add program ")
    
    student = {
        "ID"      : (valueID),
        "name"    :name,
        "age"     :age,
        "program" :program,
        "stade"   :stade
    }
    
    return student


# sumary 
def summary(value):
    print("\nSummary The Student")
    if not value:
         print("\n-----There are no Student-----\n")
    else:
        #students
        for dictionary in value:
            print(f"ID: {dictionary["ID"]} | " 
                f"name: {dictionary["name"]}  |  "
                f"age: {dictionary["age"]} | "
                f"program: {dictionary["program"]} | "
                f"stade: {dictionary["stade"]}\n")
            
# search
def search_student_ID(value):
    valueID = validation_int("Add ID student ")
    for counter in value:
        if counter["ID"] == valueID:
            print(f"ID: {counter["ID"]} | " 
                f"name: {counter["name"]}  |  "
                f"age: {counter["age"]} | "
                f"program: {counter["program"]} |"
                f"stade: {counter["stade"]}\n")    
        else: 
            print("student not found")
    return None

# update
def update_student(value): 
    # ID validation
    valueID = validation_int("Enter ID the student to update")
    
    for dictionary in value:
        cont=1
        if dictionary["ID"] == valueID:
                cont=2
                #menu creation and validation
                try:
                    print(f"\n Value to update the student {dictionary["name"]}")
                    number= int(input(
                        "1-name\n"
                        "2-age\n"
                        "3-program\n"
                        "4-stade\n"
                        "5-exit\n"
                        ":"
                    ))
                    
                    if number<=0:
                        print("You must enter a valid product (1-4)")
                        continue
                    
                    # name
                    if number ==1:
                    
                        name_new= validation_str("enter new name")
                        dictionary["name"] = name_new
    
                    # age
                    elif number ==2:
                        
                        age_new = validation_int("enter new age")
                        dictionary["age"] = age_new
                        
                    # program
                    elif number ==3:
                        
                        program_new = validation_str("enter new program")
                        dictionary["program"] = program_new
        
                    # stade
                    elif number ==4:
                        print("enter new stade")
                        stade_new = validation_str("true/ YES or flase/ NO ").lower()
                        
                        if stade_new == "yes":
                            stade_new = True
                            
                        elif stade_new == "no":
                            stade_new = False
                        else:
                            print("Enter a valid value (YES or NO)")
                            
                        dictionary["stade"] = stade_new
                        
                    # program
                    elif number ==5:
                        break
                
                    else:
                        print("You must enter a valid value (1-5)") 
                        continue  
                    
                    break
                
                except ValueError:
                    print("the value must be numeric (1-5)")
                    continue
    
    if cont == 1:
        print("\nstudent not found\n")

# Delete 
def Delete_student(value):
     # name
    valueID = validation_int("Enter ID the student to Delete")
            
    for dictionary in value:
        cont=1
        if dictionary["ID"] == valueID:
                cont=2
                value.remove(dictionary)
                print(f"\nStudent {dictionary["name"]} Delete\n")
                break
                
    
    if cont == 1:
        print(f"\nstudent  not found\n")
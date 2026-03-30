# str
def validation_str(value):
    counter_name= 1
    while counter_name == 1:
        # Request user data
        name = str(input(f"{value}: ")).strip()
        if not name.isalpha():
            print("Symbols and Numbers are not allowed")
            continue
        
        counter_name +=2
    return name

# float
def validation_float(value):
    counter_float=1
    while counter_float == 1:
        try:
            # Request user data
            v_float = float(input(f"{value}: "))
            if v_float <= 0:
                print("ERROR: Enter a valid value")
                continue
            
            break
        except ValueError:
            print("Enter a valid value")
            continue
    return float

# int 
def validation_int(value):
    
    counter_int=1
    while counter_int == 1:
        try:
            v_int = int(input(f"{value}: "))
            if v_int <=0:
                print("ERROR: Enter a value")
                continue
            break
        except ValueError:
            print("Enter a valid value")
    
    return v_int
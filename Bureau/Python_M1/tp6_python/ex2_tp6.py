def convert_to_int(value):

    value=int(input("Entrer un nombre:"))
    return int(value)
try:
    print(convert_to_int("42")) 
    print(convert_to_int(3.14))  
    print(convert_to_int("hello")) 
except ValueError as e:
    print(e)

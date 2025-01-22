class AgeInvalide(Exception):
    pass
def verifier_age(age):
    if age < 0:
        raise AgeInvalide("l'age ne peut pas etre negatif")
    


def set_age(age):
    try:
        verifier_age(age)    
    except AgeInvalide as e:
        print(e)    

print(set_age(-5))
print(set_age(5))  
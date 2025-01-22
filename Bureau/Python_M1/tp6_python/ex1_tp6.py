
def safe_division(a, b):
  if b==0:
    raise ZeroDivisionError("erreur!!")
  return a/b

try:
  test1=safe_division(2,5)
  print("le resultat de division est:",test1)

except ZeroDivisionError as erreur:
  print(erreur)



try:
  test2=safe_division(3,0)
  print("le resultat de division est:",test2)

except ZeroDivisionError as erreur:
  print(erreur)


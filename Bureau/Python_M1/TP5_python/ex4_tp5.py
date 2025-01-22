import csv
donnee=[
    ["Nom","Age","ville"],
    ["ASSIA",23,"SAFI"],
    ["NAWAL",21,"AGADIR"]   
]
with open("/home/assia/contacts.csv",mode='w',newline='')as fichier:
    ecrivain = csv.writer(fichier)
    ecrivain.writerows(donnee)
import json

etudiants = {
    "etudiants": [
         {"Nom":"SEHNANI","Age" :23,"note":16},
         {"Nom":"ELRHIRAKI","Age":21,"note":17},
         {"Nom":"NMER","Age":20,"note":15}     
    ]
}

with open("etudiants.json", "w") as fichier:
    json.dump(etudiants, fichier, ensure_ascii=False, indent=4)

with open("etudiants.json", "r", encoding="utf-8") as fichier:
    donnees = json.load(fichier)

    for etudiants in donnees["etudiants"]:
        print(f"Nom : {etudiants['Nom']}; Âge : {etudiants['Age']}; Note : {etudiants['note']}")

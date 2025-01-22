def cpt_occurence(liste):
    dic={}
    for i in liste:
        a=liste.count(i)
        dic[i]=a
    return dic
liste=['basma','nour-houda','souma','assia','assia']
print(cpt_occurence(liste))


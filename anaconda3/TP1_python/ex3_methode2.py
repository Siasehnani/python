def intersection(ensemble1 ,ensemble2):
    ensemble3=set()
    for i in ensemble1:
        for j in ensemble2:
            if i == j:
                ensemble3.add(j)
    return ensemble3
en1={'vert','rouge','blanc'}
en2={'rouge','jaune','noir'}

print(intersection(en1,en2))
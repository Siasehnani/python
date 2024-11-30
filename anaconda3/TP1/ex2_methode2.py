
def max_tuple(t):
    for i in t:
        if i>i+1 :
            max=i
            return max
t=(7,87,12,100)
print(max_tuple(t))
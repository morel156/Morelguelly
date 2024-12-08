from itertools import product
def combien_de_fois_20():
    total=0
    for combinaison in product(range(1,7),repeat=5):
        if sum(combinaison) ==20 :
            total +=1
    return total
print('''Avec 5 dés à 6 faces dont chaque dés est numérotés de 1 à 6 ,on peut 
      avoir une somme de vingts:''',combien_de_fois_20(),'''fois''')
    
    
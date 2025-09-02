i=1
r=1
""" fonction qui permet d'ecrire le factoriel d'un entier """
def factoriel(i,r):
    i=1
    r=1
    while i <= n:
        r=r*i
        i+=1
    return r 

def multiple (i):
    for i in range(1,51):
        if i%3==0:
             print(i,"GUELLY")
        if i%5==0:
             print(i,"Morel")
        if i%3==0 and i%5==0:
             print(i,"GUELLY Morel")



n=int(input("entrez un nombre:"))
print("le factoriel est",factoriel(i,r))
print(multiple(i))


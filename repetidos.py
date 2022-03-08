import random
lista = []
repetidos=[]

for i in range(0, 30):
    #lista.append(random.randint(1,100))
    lista.insert(i,random.randint(1, 100))
print(lista)

for i in lista:
    if lista.count(i) > 1 and i  not in repetidos:
        repetidos.append(i)
print(repetidos)
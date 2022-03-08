import random
lista = []
suma=0
for i in range(0, 10):
    lista.append(random.randint(1,100))
    suma+=lista[i]
media= suma / len(lista)
print(lista)
print("La Media es: ",media)


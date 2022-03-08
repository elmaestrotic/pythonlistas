import random
lista = []
veces=[]
modelos=[]
for i in range(0, 30):
    #lista.append(random.randint(1,100))
    lista.insert(i,random.randint(1, 100))
print(lista)

for i in lista:
    if lista.count(i) > 1 and i  not in modelos:
        veces.append(lista.count(i))#veces q esta ese elemento en la lista
        modelos.append(i)#guardamos el número q cumple
print('Números que más se repites:')
print(modelos)
print('veces que  se repites:')
print(veces)
print('La moda es: ' ,modelos[veces.index(max(veces))])


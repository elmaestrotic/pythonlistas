estudiantes=['Laura','Salome','Laura','Isabella','Random']
notas=[4.9,5,2.8,3,3.1]
cg=0#contador de ganadores
cp=0#contador de perdedores
indice=0
for i in notas:
    if notas[indice] < 3:
        cp+=1
    else:
        cg+=1
    indice+=1
print('Total de los que ganaron es: ',cg)
print('Total de los que no ganaron es: ',cp)

print('La nota más alta es: ',max(notas),' y la obtuvo: ',estudiantes[notas.index(max(notas))])
print('La nota más baja es: ',min(notas),' y la obtuvo: ',estudiantes[notas.index(min(notas))])
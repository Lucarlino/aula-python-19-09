import os
os.system ('cls')
#Exercício 1 
print ('Exercício 1')
listanumero = [12,31,45,86,101,120]
for valor in listanumero:
    if valor %2 == 0:
        print (valor)
print(' ')
#Exercício 2
print('Exercício 2')
listaAnimal = ['cahorro', 'leão', 'gato', 'leão']

for animal in listaAnimal:
    if animal != 'leão':
       continue
    print('O animal leão existe na lista')
    break
if 'leão' not in listaAnimal:
    print('O animal leão não existe na lista')

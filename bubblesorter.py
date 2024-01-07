lista = []
cantidad = int(input('cantidad de numeros a ordenar... '))

for index in range(cantidad):
    print('numero ',(index+1), ': ', sep='', end='')
    lista.append(int(input()))

finalizado = False
largo = len(lista)-1

while not finalizado:
    
    finalizado = True
    
    for lugar in range(largo):
        if lista[lugar] > lista[lugar+1]:
            lista[lugar], lista[lugar+1] = lista[lugar+1], lista[lugar]
            finalizado = False
            continue
  
print(lista)
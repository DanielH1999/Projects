bloques = int(input("Ingrese el número de bloques:"))
altura = 0
i = 1

while i <= bloques:
    j = 0
#    print('while', altura)# contar ejecuciones del bucle
    altura += 1
    while j <= altura:
        j += 1
    i += j
#    print('i final', i)#contar i para evaluar en la siguiente ejecucion
    
print("La altura de la pirámide:", altura)
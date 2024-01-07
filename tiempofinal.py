#preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos.
#Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.
#valores de prueba:
#12, 17, 59
#Resulta en 13:16
#23, 58, 642
#Resulta en 10:40
#0, 1, 2939
#Resulta en 1:0


hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui

dia = hora // 24                                                                #defino lo que vale un dia
duradia = (dura // 60) // 24                                                    #dura convertido a dias
durahora = dura // 60 - duradia * 24                                            #convertido a horas
duramin = dura % 60                                                             #convertido a minutos

#print('dura: ',duradia,'dias',durahora,'horas',duramin,'minutos',sep=" ")      #DEBUG DURACION

diaf = ((hora + durahora) // 24) + duradia                                      #cantidad de dias totales
horaf = (((hora + durahora) % 24) + ((min + duramin) // 60) % 24)               #cantidad de horas totales
minf = (min + duramin) % 60                                                     #cantidad de minutos totales

#print('finaliza en: ',diaf,'dias',horaf,'horas',minf,'minutos',sep=" ")        #DEBUG FINALIZACION

print(horaf,minf,sep=':')
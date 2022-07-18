#Metodo MartinGale , TDL* Calasanz
from random import randint, random
# Como aclaracion, esta simulación esta hecha en base a una ruleta americana con proporcion 2/10 verdes , 4/10 rojos y 4/10 negros , y asumiendo que apostaremos en el lado rojo o negro

apuesta = 1     # si necesita cambiar la apuesta inicial cambie el valor de esta linea
y = apuesta
repeticiones = 1 
Ganancia = 0
Perdida = 0
Ganaste = 0

while Ganaste == 0:
    print("Ronda :", repeticiones)

    x = randint(1,10)
    if x >= 5:
        print("Perdiste")
        Perdida = apuesta + Perdida
        apuesta = apuesta*2
        repeticiones = repeticiones + 1
        print("Su balance actual es de : ", Perdida*-1)
        
        

    else:
        print("Ganaste")
        Ganancia = (apuesta*2)-Perdida
        print("Su ganancia es de : ",Ganancia - apuesta)
        print("Y fueron necesarios ", apuesta," para conseguirlo")
        Ganaste = 1



# JLAM










        


from tiempo import *
from temporizador import *
if __name__ == "__main__":
    seg = int(input("Segundos:"))
    min = int(input("Minutos:"))
    hor = int(input("Horas:"))
    dia = int(input("Dias:"))
    
    time = Tiempo()
    time.establecer(seg,min,hor,dia)
    
    temp = Temporizador(time)
    clearScreen()    
    temp.iniciar()
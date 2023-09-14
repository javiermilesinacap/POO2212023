class Automovil:
    motor = ""
    encendido = False
    velocidad = 0
    def encender(self):
        self.encendido = True
    def apagar(self):
        self.encendido = False
    def acelerar(self):
        if(self.encendido):
            self.velocidad += 10
        else:
            print(chr(27)+"[1;31m","\n ATENCION: El vehículo está apagado. Encienda primero",chr(27)+"[0m")
    def frenar(self):
        self.velocidad -= 10
    def retroceder(self):
        if(self.velocidad<=0):
            self.velocidad -= 10
        else:
            print("ATENCION: No se puede retroceder mientras el vehículo está avanzando")
    def verEstado(self):
        print("\n","*-"*3,"ESTADO DEL VEHICULO","*-"*3)
        print("| Encendido: ", self.encendido, "\t\t|")
        print("| Velocidad actual : ", self.velocidad,"\t|")
        print(" *-"*10,"\n")

miautito = Automovil()

def menu():
    print("\033[7;33m")
    print("1 para encender")
    print("2 para apagar")
    print("3 para acelerar")
    print("4 para frenar")
    print("5 para retroceder")
    print("0 para salir")
    print("\033[0m")
    print("\033[2;32m")
    opcion = int(input("Ingrese opción: "))
    print("\033[0m")
    print("\033[2J")
    if(opcion==1):
        miautito.encender()
    elif(opcion == 2):
        miautito.apagar()
    elif(opcion==3):
        miautito.acelerar()
    elif(opcion==4):
        miautito.frenar()
    elif(opcion==5):
        miautito.retroceder()
    elif(opcion==0):
        exit()
    miautito.verEstado()

while(True):
    menu()

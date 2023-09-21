# Actividad: Implementar clases para cualquier figura geométrica. 
class Unidimensional: 
    # (self, x=0.0, y=0.0) -> Aplica Polimorfismo. Se puede llamar como Unidimensional() y Unidimensional(2,5)
    def __init__(self, x=0.0, y=0.0):
        try: 
            self.x = float(x)
            self.y = float(y)
        except: 
            print("Error: Revise los parámetros de entrada")
    def getX(self):
        return self.x 
    def getY(self):
        return self.y
    def setX(self, x):
        try:
            self.x = float(x)
        except: 
            print("El valor no es numérico")
    def setY(self, y):
        try: 
            self.y = float(y)
        except: 
            print("El valor no es numérico")
class Bidimensional: 
    def __init__(self):
        self.points = []
    
#Creo un Objeto
objeto = Unidimensional(4,6)
#Muestro los valores del objeto
print("El valor de X es: ", objeto.getX(), ",",objeto.getY() )

objeto1 = Bidimensional()
print(objeto1.points)



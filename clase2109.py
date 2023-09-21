# Actividad: Implementar clases para cualquier figura geométrica. 
class Unidimensional: 
    def __init__(self):
        self.x = 0
        self.y = 0
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

#Creo un Objeto
objeto = Unidimensional()
#Muestro los valores del objeto
print("El valor de X es: ", objeto.getX())
print("El valor de Y es: ", objeto.getY())



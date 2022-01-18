class VerificarEdad:
            
    def __init__(self): # Constructor de la clase 
        self.edad = None
        self.tomar_dato = None
        
    def mayor_edad(self):
        print('Dime tu edad')
        self.tomar_dato = input()
        self.edad = int(self.tomar_dato)
        
        if self.edad >= 18:
            print('Eres mayor de edad')
        else:
            print('Eres menor de edad')
            
        print('Programa Terminado')
        
    def rango_edad(self):
        print('Dime tu edad')
        self.tomar_dato = input()
        self.edad = int(self.tomar_dato)
        
        if self.edad >= 65:
            print('Eres de la tercera edad')
        elif self.edad >= 18:
            print('Eres mayor de edad')
            
        else:
            print('Eres menor de edad')
            
        print('Programa Terminado')


ver_edad = VerificarEdad()

ver_edad.rango_edad()
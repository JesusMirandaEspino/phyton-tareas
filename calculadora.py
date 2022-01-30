class calculadora:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.init = True
        self.select = None

    def sumar(self):
        self.ingresar_numeros()
        try:
            suma = self.num1 + self.num2
            print("el resultado de la suma es: ", suma)
        except TypeError as error:
            print('No se puede sumar un tipo entero con un tipo string', error)

    def restar(self):
        self.ingresar_numeros()
        try:
            resta = self.num1 - self.num2
            print("el resultado de la resta es: ", resta)
        except TypeError as error:
            print('No se puede restar un tipo entero con un tipo string', error)


    def multiplicar(self):
        self.ingresar_numeros()
        
        
        try:
            multiplicacion = self.num1 * self.num2
            print("el resultado de la multiplicación es: ", multiplicacion)
        except TypeError as error:
            print('No se puede multlipicar un tipo entero con un tipo string, puede existir algun error, favor de verificar', error)
            

    def dividir(self):
        
        self.ingresar_numeros()
        try:
            divicion = self.num1 / self.num2
            print("el resultado de la divición es: ", divicion)
        except (ZeroDivisionError, TypeError) as error:
            print('No se puede dividir entre cero, o  hacer una divicion con un string incluido', error)
            print('Intenta dividir entre un numero mayor a cero')

    def salir(self):
        self.init = False
    
    def ingresar_numeros(self):
        
        try:
            self.num1 = float(input("ingrese un numero: "))
        except ValueError as error:
            print('No se puede usar un tipo string. para realizar una operacion', error)

        try:
            self.num2 = float(input("ingrese un numero: "))
        except ValueError as error:
            print('No se puede usar un tipo string. para realizar una operacion', error)
            print('Si devuelve un resultado con string, favor de verificar, puede existir un error')

    def menu(self):
        
        while self.init:
            print('Elige que operacion deseas realizar')
            print('1.- Suma')
            print('2.- Resta')
            print('3.- Division')
            print('4.- Multiplicacion')
            print('5.- Salir')

            self.select = input()
            
            if self.select == '1':
                self.sumar()
            elif self.select == '2':
                self.restar()
            elif self.select == '3':
                self.dividir()
            elif self.select == '4':
                self.multiplicar()
            elif self.select == '5':
                self.salir()
                print('Programa Terminado. Ten Un buen dia')
            else:
                print('Hubo un error, Por favor elige nuevamente')
                


ejecutar_calculadora = calculadora()

ejecutar_calculadora.menu()

#calculadora.sumar()
#calculadora.multiplicar()
#calculadora.restar()
#calculadora.dividir()
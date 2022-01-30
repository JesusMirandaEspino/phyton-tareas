# Online Python compiler (interpreter) to run Python online.
class Persona(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        
    def print_title(self):
        if self.sex == "masculino":
            print("¡Es un hombre!")
        elif self.sex == "femenino":
            print("¡Es una mujer!")

class Child(Persona):                # Niño hereda Persona
    def print_title(self):
        if self.sex == "masculino":
            print("¡Es un chico!")
        elif self.sex == "femenino":
            print("¡Es una chica!")
        
Mayra = Child("Mayra","femenino")
Pedro = Persona("Pedro","masculino")

print(Mayra.name,Mayra.sex,Pedro.name,Pedro.sex)
Mayra.print_title()
Pedro.print_title()

# imprimir nombre, sexo, edad, si es hombre o mujer, niño o adulto
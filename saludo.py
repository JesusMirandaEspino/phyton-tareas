class Saludar:
            
    def __init__(self): # Constructor de la clase 
        self.saludo = '“Hola a todos, Hola Kuepa”.'
        
    # Metodo para mostrar los datos de la lista
    def __str__(self):
        # Muestra el saludo
        return str(self.saludo)
    
saludando = Saludar()

print(saludando)
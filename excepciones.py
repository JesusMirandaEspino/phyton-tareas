SEPARADOR1 = '************************************************************'
SEPARADOR2 = '**                                                        **'

def division():
    x = 10/0
    return x
try:
    division()
except ZeroDivisionError as error:
    print('No se puede dividir entre cero', error)
    print('Intenta dividir entre un numero mayor a cero')
    
print(SEPARADOR1)
print(SEPARADOR2)

lista = [1, 2, 3, 4, 5]
try:
    print(lista[10])
except IndexError as error:
    print('No existe el indice seleccionado en la lista', error)
    print('Intenda un indice menor o igual a: ',  str( len(lista) ) )

print(SEPARADOR1)
print(SEPARADOR2)

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
try:
    print(colores['blanco'])
except KeyError as error:
    print('No existe el elemento seleccionado en la lista', error)
    print('Intenda con alguno de los siguientes elementos: ',  str( colores ) )

print(SEPARADOR1)
print(SEPARADOR2)

try:
    resultado = 15 + "20"
    print(resultado)
except TypeError as error:
    print('No se puede sumar un tipo entero con un tipo string', error)
    print('Intenda algo como 15 + 20, sin poner comillas, o en el input algo como: ' )
    print('int(input()), para cada valor y despues realiza la suma ', )
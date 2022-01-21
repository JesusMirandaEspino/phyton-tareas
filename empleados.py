import string

class Empleado:
    nombre_emp: string
    dpto_emp: string
    puesto_emp: string
    
    def establecer_nombre_emp(self, nom: string):
        self.nombre_emp = nom
        
    def establecer_depto_emp(self, dpto: string):
        self.dpto_emp = dpto
        
    def establecer_puesto_emp(self, puesto: string):
        self.puesto_emp = puesto
    
    def obtener_nombre_emp(self):
        return self.nombre_emp
    
    def obtener_depto_emp(self):
        return self.dpto_emp
    
    def obtener_puesto_emp(self):
        return self.puesto_emp



class EmpPorHoras(Empleado):

    horas_trabajo: string
    cuota_hora: float
    sueldo_qna_horas: float
        
    def establecer_horas_trab(self, horas_trabajo: int):
        self.horas_trabajo = horas_trabajo
        
    def establecer_cuota_hora(self, cuota_hora: int):
        self.cuota_hora = cuota_hora

    def calcular_sueldo_qna_horas(self):
        self.sueldo_qna_horas = self.horas_trabajo * self.cuota_hora
        
    def obtener_sueldo_qna_horas(self):
        return self.sueldo_qna_horas
    
    
    
class  EmpAsalariado(Empleado):
    
    sueldo_mensual: float
    sueldo_qnal: float
    
    def establecer_sueldo_mensual(self, sdo: float):
        self.sueldo_mensual = sdo
        
    def calcular_sueldo_qna_asal(self):
        self.sueldo_qnal = self.sueldo_mensual / 2
        
    def obtener_sueldo_qna_asal(self):
        return self.sueldo_qnal
    
    
class ejecuta_empleado:
    
    nombre_emp: string
    dpto_emp: string
    puesto_emp: string
    horas_trabajo: string
    cuota_hora: float
    sueldo_qna_horas: float
    sueldo_mensual: float
    sueldo_qnal: float 
    
    
print( 'Selection Tipo de empleado: ' )

print( '1.- Empleado por horas ' )
print( '2.- Empleado Asalariado ' )
print( 'Nota: Escribe solo el numero seleccionado' )

tomar_dato = input()
    

if tomar_dato == '1':
    nuevoempleado = EmpPorHoras()
    
    print( 'Por favor Ingresa su nombre' )
    tomar_nombre = input()
    nuevoempleado.establecer_nombre_emp(tomar_nombre)
    
    print( 'Por favor Ingresa su Departamento' )
    tomar_departamento = input()
    nuevoempleado.establecer_depto_emp(tomar_departamento)
    
    print( 'Por favor Ingresa su Puesto' )
    tomar_puesto = input()
    nuevoempleado.establecer_puesto_emp(tomar_puesto)
    
    print( 'Por favor Ingresa sus horas trabajadas' )
    tomar_horas = int(input())
    nuevoempleado.establecer_horas_trab(tomar_horas)
    
    print( 'Por favor Ingresa el costo por hora trabajada' )
    tomar_horas_costo = int(input())
    nuevoempleado.establecer_cuota_hora(tomar_horas_costo)
    
    nuevoempleado.calcular_sueldo_qna_horas()
    
    print( 'Resultado: ' )
    print( 'Nombre: ' + str(nuevoempleado.obtener_nombre_emp() ))
    print( 'Departamento: ' + str(nuevoempleado.obtener_depto_emp() ))
    print( 'Puesto: ' + str(nuevoempleado.obtener_puesto_emp() ))
    print( 'Sueldo Quincenal: ' + str(nuevoempleado.obtener_sueldo_qna_horas() ))

elif tomar_dato == '2':
    nuevoempleado = EmpAsalariado()
    
    print( 'Por favor Ingresa su nombre' )
    tomar_nombre = input()
    nuevoempleado.establecer_nombre_emp(tomar_nombre)
    
    print( 'Por favor Ingresa su Departamento' )
    tomar_departamento = input()
    nuevoempleado.establecer_depto_emp(tomar_departamento)
    
    print( 'Por favor Ingresa su Puesto' )
    tomar_puesto = input()
    nuevoempleado.establecer_puesto_emp(tomar_puesto)
    
    print( 'Por favor Ingresa su salario Mensual' )
    tomar_sueldo = int(input())
    nuevoempleado.establecer_sueldo_mensual(tomar_sueldo)

    nuevoempleado.calcular_sueldo_qna_asal()
    
    print( 'Resultado: ' )
    print( 'Nombre: ' + str(nuevoempleado.obtener_nombre_emp() ))
    print( 'Departamento: ' + str(nuevoempleado.obtener_depto_emp() ))
    print( 'Puesto: ' + str(nuevoempleado.obtener_puesto_emp() ))
    print( 'Sueldo Quincenal: ' + str(nuevoempleado.obtener_sueldo_qna_asal() ))

else:
    print('Error al elegir')
        
"""   

5. Leer nomEmp, depto, puesto

"""
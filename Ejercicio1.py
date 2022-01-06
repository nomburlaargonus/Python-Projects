class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    def mostrar (self):
        print(f"Nombre:{self.nombre} \nEdad:{self.edad} \nDni:{self.dni}")

    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False
    

sebastian = Persona("sebastian", 23, 20132567)

sebastian.mostrar()



class Cuenta:
    def __init__(self, individuo=Persona(), cantidad=0.0):
        self.individuo = individuo
        self.__cantidad = cantidad

    def mostrar(self, mostrar):
        self.individuo.mostrar()

    def ingresar(self, monto_i):
        if monto_i > 0:
            self.__cantidad += monto_i
        else:
            print("Ingreso un monto negativo")
        print(f"saldo disponible {self.__cantidad}")

    def retirar(self, monto_r):
        if monto_r > 0:
            self.__cantidad -= monto_r
        else:
            print("Ingreso un monto negativo")
        print(f"Saldo disponible {self.__cantidad}")




cuenta_1 = Cuenta(sebastian, 1000)

cuenta_1.ingresar(270)

cuenta_1.retirar(2000)
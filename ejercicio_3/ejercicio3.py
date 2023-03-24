import random
from datetime import datetime, timedelta

class CuentaBancaria:
    id_cuenta = 0

    def __init__ (self, nombre_titular):
        self.id_cuenta = CuentaBancaria.generar_id_cuenta() #id de cuenta
        self.nombre_titular = nombre_titular
        self.fecha_apertura = datetime.now()
        self.num_cuenta = random.randit(10**11,10**12-1) #numero de cuenta aleatorio de 12 digitos
        self.saldo = 10000.00 

    def retirar_dinero(self,cantidad):
        if cantidad > self.saldo:
            print("No tienes suficiente dinero en cuenta")
        elif cantidad <= self.saldo:
            print (f"Se han retirado {cantidad} euros de la cuenta {self.num_cuenta}, Nuevo saldo; {self.saldo} euros.")
    
    def ingresar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"Se han ingresado {cantidad} euros en la cuenta {self.num_cuenta}. Nuevo saldo: {self.saldo} euros")
    
    def transferir_dinero(self, otra_cuenta, cantidad):
        if cantidad > self.saldo:
            print("No se puede transferir esa cantidad de dinero, no tienes suficiente dinero")
        else:
            self.saldo -= cantidad
            otra_cuenta.saldo += cantidad
            print(f"Se han transferido{cantidad} euros de la cuenta {self.num_cuenta} a la cuenta {otra_cuenta.num_cuenta}. Saldo actual en la cuenta {self.num_cuenta}: {self.saldo} euros")
        classmethod
        def generar_id_cuenta(cls):
            cls.id_cuenta += 1
            return cls.id_cuenta
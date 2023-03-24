from ejercicio_3.banco.CuentaBancaria import CuentaBancaria
import random
from datetime import datetime, timedelta

class CuentaPlazoFijo(CuentaBancaria):
    def __init__(self, nombre_titular):
        super().__init__(nombre_titular)
        self.fecha_vencimiento = self.fecha_apertura + timedelta(days=random.randit(30,365))
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            print("No se puede retirar esa cantidad de dinero porque no tienes suficiente saldo")
        elif datetime.now() < self.fecha_vencimiento:
            print("No se puede retirar dinero antes de la fecha de vencimiento.")
        else: 
            penalizacion = cantidad * 0.05
            self.saldo -= (cantidad + penalizacion)
            print(f"Se han retirado {cantidad} euros de la cuenta { self.num_cuenta} antes de la fecha de vencimiento. Se ha aplicado una penalización del 5%({penalizacion} euros). Nuevo saldo: {self.saldo} euros. ")
            

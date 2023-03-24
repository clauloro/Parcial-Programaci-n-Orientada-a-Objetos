from ejercicio_3.banco.CuentaBancaria import CuentaBancaria


class CuentaVIP(CuentaBancaria):
    saldo_max_negativo = -1000.0
    
    def __init__(self, nombre_titular):
        super().__init__(nombre_titular)
        
    def retirar_dinero(self, cantidad):
        if cantidad <= self.saldo or self.saldo - cantidad >= CuentaVIP.saldo_max_negativo:
            self.saldo -= cantidad
            print("Se han retirado", cantidad, "euros de la cuenta.")
        else:
            print("No se puede retirar esa cantidad de dinero. El saldo negativo supera el límite permitido.")
            
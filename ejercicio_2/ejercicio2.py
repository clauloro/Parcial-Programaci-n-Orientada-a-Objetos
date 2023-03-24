class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Mamifero(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tipo = "Mamífero"

    def amamantar(self):
        print("Amamantando a las crías")


class Oviparo(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tipo = "Ovíparo"

    def poner_huevos(self):
        print("Poniendo huevos")


class Pollo(Oviparo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tipo = "Pollo"


class Gato(Mamifero):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tipo = "Gato"

class Ornitorrinco(Mamifero, Oviparo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tipo = "Ornitorrinco"

    def poner_huevos(self):
        print("Poniendo huevos de ornitorrinco")

    def amamantar(self):
        print("Amamantando crías de ornitorrinco")

    def sonido(self):
        print("Sonidos extraños de ornitorrinco")



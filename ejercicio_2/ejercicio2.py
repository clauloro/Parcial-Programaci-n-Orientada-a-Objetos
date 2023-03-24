class Animal:
    
    pass

class Mamifero(Animal):
    pass

class Oviparo(Animal):
    pass

class Pollo(Oviparo):
    pass

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Oviparo):
    pass

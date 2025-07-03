# calculadora.py

class Calculadora:
    def __init__(self):
        self._numero1 = 0
        self._numero2 = 0

    # Getter y Setter para numero1
    def get_numero1(self):
        return self._numero1

    def set_numero1(self, valor):
        self._numero1 = valor

    # Getter y Setter para numero2
    def get_numero2(self):
        return self._numero2

    def set_numero2(self, valor):
        self._numero2 = valor

    def sumar(self):
        return self._numero1 + self._numero2

    def restar(self):
        return self._numero1 - self._numero2

    def multiplicar(self):
        return self._numero1 * self._numero2

    def dividir(self):
        if self._numero2 == 0:
            raise ValueError("No se puede dividir por cero")
        return self._numero1 / self._numero2

    def potenciar(self):
        return self._numero1 ** self._numero2

    def raiz(self):
        if self._numero2 == 0:
            raise ValueError("El índice de la raíz no puede ser cero")
        return self._numero1 ** (1 / self._numero2)

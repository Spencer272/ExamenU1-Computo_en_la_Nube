# -*- coding: utf-8 -*-
"""mi_funcion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UJq3H6sk0qpyUkiTbOITPWHC4nldjrE-
"""

# Celda 1 en Google Colab
def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
# Comprobar si el número es divisible por algún impar desde 3 hasta la raíz cuadrada de 'numero'
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True
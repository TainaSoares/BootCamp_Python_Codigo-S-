"""
STONE TECH - CÓDIGO[S]

EXERCÍCIO 3

TEMA: Tipos numéricos

Programa que recebe os 3 lados de um triãngulo e imprima sua área:
"""

import math


lado_1 = float(input("Insira o primeiro lado do triângulo: "))
lado_2 = float(input("Insira o segundo lado do triângulo: "))
lado_3 = float(input("Insira o terceiro lado do triângulo: "))

lado = (lado_1 + lado_2 + lado_3) / 2

area = math.sqrt(lado*(lado - lado_1)*(lado - lado_2)*(lado - lado_3))

print(f"\n A área do triângulo de lados {lado_1}m , {lado_2}m e {lado_3}m é {area:.2f}m2")
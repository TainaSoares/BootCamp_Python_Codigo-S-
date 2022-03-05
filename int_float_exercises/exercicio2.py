"""
STONE TECH - CÓDIGO[S]

EXERCÍCIO 2

TEMA: Tipos numéricos

Programa que recebe base e altura de um triãngulo e imprima sua área:
"""

base = float(input("Insira a base do triângulo: "))
altura = float(input("Insira a altura do triângulo: "))

area = (base * altura) / 2

print(f"\n A área do triângulo de base {base}m e altura {altura}m é {area:.2f}m2")
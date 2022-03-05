"""
STONE TECH - CÓDIGO[S]

EXERCÍCIO 4

TEMA: Tipos numéricos

Programa que recebe peso em kg e altura em m e calcula o IMC:
"""

import math


peso = float(input("Insira seu peso em kg: "))
altura = float(input("Insira sua altura em m: "))

IMC = peso / (math.pow(altura,2))

print(f"\nO IMC de uma pessoa com peso {peso}kg e altura {altura}m é: {IMC:.2f}\n")
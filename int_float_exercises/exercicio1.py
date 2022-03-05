"""
STONE TECH - CÓDIGO[S]

EXERCÍCIO 1

TEMA: Tipos numéricos

Programa que recebe dois números inteiros do usuário, A e B e 
imprime na tela as seguintes operações:
"""

import math

numero_A = int(input("Insira um número : "))
numero_B = int(input("Insira um número : "))

# Operações

soma = numero_A + numero_B
print(f"\nA soma dos números resulta em : {soma}\n")

diferenca = numero_B - numero_A
print(f"\nA diferença dos números resulta em : {diferenca}\n")

produto = numero_A * numero_B
print(f"\nO produto dos números resulta em : {produto}\n")

quociente = numero_A // numero_B
print(f"\nO quociente dos números resulta em : {quociente}\n")

resto = numero_A % numero_B
print(f"\nO resto da divisão resulta em : {resto}\n")

log_A = math.log10(numero_A)
print(f"\nO log de {numero_A} na base 10 resulta em : {log_A:.2f}\n")

# expo = numero_A ** numero_B  ---- também funciona
expo = math.pow(numero_A,numero_B)
print(f"\nO número {numero_A} elevado a {numero_B} resulta em : {expo}\n")


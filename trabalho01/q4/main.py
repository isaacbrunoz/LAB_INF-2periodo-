# Questão 4 - Verificador de Números Pares e Ímpares
# Crie uma função que receba um número inteiro e retorne se ele é par ou ímpar.

import par

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")
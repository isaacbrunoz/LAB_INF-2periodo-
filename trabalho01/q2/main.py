# Q2 - Conversor de Temperatura
# Conversão entre Celsius e Fahrenheit
# Obrigração: criar um arquivo conversor.py e importar as funções

import conversor

print("Conversor de Temperatura")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
opcao = int(input("Escolha uma opção (1 ou 2): "))

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = conversor.celsius_for_fahrenheit(celsius)
    print(f"{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F.")

elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = conversor.fahrenheit_for_celsius(fahrenheit)
    print(f"{fahrenheit:.2f}°F equivalem a {celsius:.2f}°C.")
else:
    print("Opção inválida.")
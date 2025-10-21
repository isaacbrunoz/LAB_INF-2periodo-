def calcular_imposto(preco):
  
  return preco * 1.15

try:
 
  preco_digitado = float(input("Digite o preço do produto: R$ "))

  preco_com_imposto = calcular_imposto(preco_digitado)

  print(f"O valor com 15% de imposto é: R$ {preco_com_imposto:.2f}")

except ValueError:
  print("Erro: Por favor, digite um número válido.")
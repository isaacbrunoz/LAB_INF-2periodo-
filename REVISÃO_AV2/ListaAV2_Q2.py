def calcular_desconto(preco):
  
  return preco * 0.90

try:
 
  preco_digitado = float(input("Digite o preço do produto: R$ "))

  preco_com_desconto = calcular_desconto(preco_digitado)

  print(f"O valor com 10% de desconto é: R$ {preco_com_desconto:.2f}")

except ValueError:
  print("Erro: Por favor, digite um número válido.")
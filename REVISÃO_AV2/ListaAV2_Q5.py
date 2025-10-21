def calculador_imc(peso, altura):
   imc = peso/(altura**2)
   return imc

def classificar_imc(valor_imc):
   if valor_imc < 18.5:
      return "Abaixo do peso."
   elif valor_imc < 25:
      return "Peso normal."
   else:
      return "Acima do peso."
   
try:
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    valor_imc = calculador_imc(peso, altura)

    classificacao = classificar_imc(valor_imc)

    print(f"\nSeu IMC é: {valor_imc:.2f}")
    print(f"Classificação: {classificacao}")


except ValueError:
  print("ERRO: Digite um número inteiro.")

except ZeroDivisionError:
  print("ERRO: A altura não pode ser zero.")


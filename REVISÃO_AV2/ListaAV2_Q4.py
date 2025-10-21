def analise_idade(idade):

    if idade >= 18:
        return "Maior de idade."
    else:
        return "Menor de idade."
    
try:
    idade_digitada = int(input("Digite a sua idade: "))

    status = analise_idade(idade_digitada)

    print(status)

except ValueError:
  print("ERRO: Digite um número inteiro.")
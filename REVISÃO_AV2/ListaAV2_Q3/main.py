from funcoes_bolsa import verificar_acoes


try:
    valor_digitado = float(input("Digite o valor da ação: R$ "))

    resultado = verificar_acoes(valor_digitado)

    print(resultado)

except ValueError:
    print("ERRO: Digite um número válido.")
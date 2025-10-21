# Professor, estava fazendo as 4 questões de try...except e -
# percebi que elas eram bem parecidas em alguns quesitos.
# Dito isso, tentei juntar as 4 questões em 1 codigo só. 
# Espero que não seja problema ;)


def dividir(numero1, numero2):
   
    try:
        return numero1 / numero2
    except ZeroDivisionError:
        
        return "ERRO: Não é possível dividir por zero."

try:
    
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))

    resultado = dividir(numero1, numero2)
    
    if resultado == "ERRO: Não é possível dividir por zero.":
        print(resultado)
    else:
        print(f"A divisão é igual a: {resultado:.2f}")

except ValueError:
    print("ERRO: Digite um número válido.")

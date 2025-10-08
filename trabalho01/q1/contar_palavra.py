def contar_palavra(frase, palavra):

    frase_minuscula = frase.lower()
    palavra_minuscula = palavra.lower()
    palavra_frase = frase_minuscula.split()

    return palavra_frase.count(palavra_minuscula)
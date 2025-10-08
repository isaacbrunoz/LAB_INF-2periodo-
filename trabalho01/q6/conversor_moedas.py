def conversor_moedas(valor, cotacao, tipo= 'real_for_dolar'):
    if tipo == 'real_for_dolar':
        return valor / cotacao
    elif tipo == 'dolar_for_real':
        return valor * cotacao
    else:
        return None

def autenticador(usuario, senha, usuarios_cadastrados):
    if usuario in usuarios_cadastrados:
        if usuarios_cadastrados[usuario] == senha:
            return "Autenticado!"
        else:
            return "Senha incorreta"
        
    else:
        return "Usuário não encontrado."

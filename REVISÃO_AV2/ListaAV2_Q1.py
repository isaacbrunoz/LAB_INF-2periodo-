def verificar_login(email, senha):

    if email == 'admin' and senha =='admin':
     return True
    
email_usuario = input("Digite seu email: ")
senha_usuario = input("Digite sua senha: ")

if verificar_login(email_usuario, senha_usuario):
   print("Login feito com sucesso!")

else:
   print("Email ou senha incorretos.")
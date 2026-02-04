import getpass


##simples cadastro de usuario
usuarios = []
def cadastrar_user():
    while True:
        user = input('Digite seu nome de usuario\n').strip()
        if ' ' in user:
            print('Usuario não pode conter espaço')
            continue
        if len(user) < 5:
            print('Usuario invalido, tem que ter no minimo 5 letras')
            continue
        else :
            return user


import getpass

def cadastrar_senha():
    while True:
        senha = getpass.getpass('Digite sua senha:\n').strip()

        if ' ' in senha:
            print('Senha não pode conter espaços')
            continue

        if len(senha) < 8:
            print('Senha inválida, coloque no mínimo 8 caracteres\n')
            continue

        return senha
    

user = cadastrar_user()
senha = cadastrar_senha()
user_cadastro = {user : senha}
usuarios.append(user_cadastro)

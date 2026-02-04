
informacoes_usuario =[]


def recolher_informacoes(texto):
    #essa e uma funçao geral para recolher o texto
    """
    recebe um texto como parametro, e retorna o input desse texto 
    """
    info = input(texto)
    return info.strip()

def cadastrar_usuario():
    """
    aqui voce pode cadastrar o usuario,
    rece um como output o nome, idade e o nome da cidade
    """


    subtitulo('Você escolheu cadastrar seu usuário\n')
    nome = recolher_informacoes('Digite seu nome\n').lower()
    while True:
        try:
            idade = int(recolher_informacoes('Digite sua idade\n').strip())
            break
        except ValueError:
            print('Apenas números por favor!')
    cidade = recolher_informacoes('Selecione sua cidade\n').lower()
    dados_usuario = {'nome': nome, 'idade': idade, 'cidade': cidade}
    informacoes_usuario.append(dados_usuario)
    print(informacoes_usuario)

def alterar_idade(usuario_para_alterar):
    """
    aqui voce pode alterar uma idade cadastrada errado, ou apos um aniversario
    input:nova idade
    output:cadastra nova idade na lista
    """
    while True:
        try:
            nova_idade = int(recolher_informacoes('Digite a nova idade a ser inserida'))
            usuario_para_alterar['idade'] = nova_idade
            print("Alterado com sucesso")
            return
        except ValueError:
            print('Apenas números')

def alterar_nome(usuario_para_alterar):
    """
    aqui voce altera o nome
    input: novo nome
    output:altera o nome no dicionario na lista
    """
    novo_nome = recolher_informacoes('Digite o novo nome')
    usuario_para_alterar['nome'] = novo_nome
    print('Alterado com sucesso')

def alterar_cidade(usuario_para_alterar):
    """
    aqui voce altera o nome da cidade
    input: nova cidade
    output:altera o nome da cidade no dicionario na lista
    """
    nova_cidade = recolher_informacoes('Digite a nova cidade')
    usuario_para_alterar['cidade'] = nova_cidade
    print('Alterado com sucesso')

def verificar_usuario():
    """
    aqui você verifica se o usuario está cadastrado 
    input: usuario para buscar
    output: se o user está cadastrado
    """
    usuario_para_alterar = recolher_informacoes('Digite o nome do cadastro que deseja alterar\n').lower()
    for usuario in informacoes_usuario:
        if usuario['nome'] == usuario_para_alterar:
            return usuario
    print('Cadastro não encontrado')
    return None

def menu_alteracoes():
    subtitulo('Menu de Alterações\n')
    usuario = verificar_usuario()
    
    if usuario is None:
        return
    
    while True:
        print('\n--- Alterar Dados ---')
        print('1. Alterar Nome')
        print('2. Alterar Idade')
        print('3. Alterar Cidade')
        print('4. Voltar ao Menu Principal')
        
        opcao = recolher_informacoes('\nEscolha uma opção: ')
        
        if opcao == '1':
            alterar_nome(usuario)
        elif opcao == '2':
            alterar_idade(usuario)
        elif opcao == '3':
            alterar_cidade(usuario)
        elif opcao == '4':
            break
        else:
            print('Opção inválida!')

def listar_usuarios():
    subtitulo('Lista de Usuários Cadastrados\n')
    
    if not informacoes_usuario:
        print('Nenhum usuário cadastrado ainda.')
        return
    
    for i, usuario in enumerate(informacoes_usuario, 1):
        print(f"{i}. Nome: {usuario['nome'].title()} | Idade: {usuario['idade']} | Cidade: {usuario['cidade'].title()}")

def excluir_usuario():
    subtitulo('Excluir Usuário\n')
    
    if not informacoes_usuario:
        print('Nenhum usuário cadastrado para excluir.')
        return
    
    nome_para_excluir = recolher_informacoes('Digite o nome do usuário que deseja excluir: ').lower()
    
    for usuario in informacoes_usuario:
        if usuario['nome'] == nome_para_excluir:
            informacoes_usuario.remove(usuario)
            print(f'Usuário {nome_para_excluir.title()} excluído com sucesso!')
            return
    
    print('Usuário não encontrado.')

def subtitulo(texto):
    print('\n' + '=' * 40)
    print(texto)
    print('=' * 40)

def menu_principal():
    while True:
        subtitulo('SISTEMA DE CADASTRO DE USUÁRIOS')
        print('1. Cadastrar novo usuário')
        print('2. Listar usuários cadastrados')
        print('3. Alterar dados de usuário')
        print('4. Excluir usuário')
        print('5. Sair')
        
        opcao = recolher_informacoes('\nEscolha uma opção: ')
        
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            menu_alteracoes()
        elif opcao == '4':
            excluir_usuario()
        elif opcao == '5':
            print('\nEncerrando o sistema. Até logo!')
            break
        else:
            print('Opção inválida! Tente novamente.')



#executar o programa
if __name__ == '__main__':
    menu_principal()
produtos_cadastrados = []

def menu_inicial():
    print('Sistema X')
    escolha_user = int(input('Escolha sua opção\n' \
    '1.Consultar produtos\n' \
    '2.Cadastrar um produto\n' \
    '3.Alterar um estoque\n' \
    '4.Itens zerados\n'
    '5.Sair\n'))
    return escolha_user

def cadastrar_produto():
    ##aqui o usuario pode cadastrar o produto dele, tinha usado indice 0 antes, mas ai buga tudo
    nome_produto = input('Insira o nome do produto a ser cadastrado\n').lower()
    quantidade_produto = int(input('Digite a quantidade inicial em estoque\n'))
    dados_produto = {'nome': nome_produto, 'estoque': quantidade_produto}
    produtos_cadastrados.append(dados_produto)
    print(f'Você está cadastrando o produto {produtos_cadastrados[-1]['nome']}, com {produtos_cadastrados[-1]['estoque']} unidades no estoque')

def pesquisar_produto():
    ##aqui o usuario pode pesquisar so por um produto especifico
    ##talvez eu volte para adicionar alguma outra função
    nome_alterar = input('Digite o nome do produto que você deseja alterar no estoque: \n').lower()
    for i in produtos_cadastrados:
        if i['nome'] == nome_alterar:
            print(f'Produto encontrado: {i['nome']}, estoque: {i['estoque']}')
            return

def alterar_estoque(): 
    #aqui o usuario pesquisa pelo item que quer alterar o estoque e o altera

    nome_alterar = input('Digite o nome do produto que você deseja alterar no estoque: \n').lower()
    for i in produtos_cadastrados:
        if i['nome'] == nome_alterar:
            novo_estoque = int(input('Insira a quantidade a alterar\n'))
            i['estoque'] = novo_estoque
            print(f'Estoque de {i['nome']} atualizado para {i['estoque']} unidades')
            return
    print('Produto não encontrado!')

def listar_produtos():
    #aqui mostra todos os produtos na lista
    if not produtos_cadastrados:
        print('Nenhum produto cadastrado!')
        return
    for i in produtos_cadastrados:
        print(f'Produto: {i['nome']}, estoque: {i['estoque']}')     

def consulta_zerado():
    ##aqui consulta se algum dos itens está com o estoque zerado
    zerados = False
    for i in produtos_cadastrados:
        if i['estoque'] == 0:
            print(f'Produto {i['nome']} está com o estoque zerado!')
            zerados = True
    if not zerados:
        print('Nenhum produto com estoque zerado!')

def main():
    while True:
        try:
            escolha_user = menu_inicial()
            if escolha_user == 1:
                listar_produtos()
            elif escolha_user == 2:
                cadastrar_produto()
            elif escolha_user == 3:
                alterar_estoque()
            elif escolha_user == 4:
                consulta_zerado()
            elif escolha_user == 5: 
                print('Saindo do sistema...')
                break
            else: 
                print('Escolha um número válido')
        except ValueError:
            print('Digite apenas números por favor')

if __name__ == '__main__':
    main()
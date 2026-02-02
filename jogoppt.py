import random

#sao 3 listas para pedra papel e tesoura, dessa forma, cada lista automaticamente ja faz o usuario setar o valor, e o bot so prec
#assim acho q fica mais facil do bot ler doq varios if e elses
PEDRA = ['Tesoura',
         'Pedra',
         'Papel']
PAPEL = ['Pedra',
         'Papel',
         'Tesoura']
TESOURA = ['Papel',
           'Tesoura',
           'Pedra']

LISTA_JOGADAS = [PEDRA,PAPEL,TESOURA]
NOMES = ['Pedra','Papel','Tesoura']

vitorias_ppt = 0
derrotas_ppt = 0
empates_ppt = 0
jogos = 0
erros = 0
tentativas_totais = 0


def menu_geral():#menu que vai rodar em loop e selecionar qual função vamos executar
    while True:
        try:
            print('Bem vindo ao seu único amigo')
            jogo_selecionado = int(input('Escolha o jogo que vamos jogar hoje:\n'
                    '1. Pedra, papel e tesoura\n' \
                    '2. Jogo da adivinhação\n'
                    '3. Batalha Naval\n'
                    '4. Placar\n'
                    '5. Sair\n' ))
            if jogo_selecionado not in (1, 2, 3, 4, 5):
                print('Escolha uma opção válida')
            elif jogo_selecionado == 3:
                print('Você sabe que eu ainda não sei fazer isso né?')
            else:
                return jogo_selecionado
        
        except ValueError:
            print('Digite apenas números por favor')

def jogo_ppt(): #aqui o user escolhe a jogada dele, e com base nela escolhemos qual lista vamos usar para comparar se ganhou ou perdeu
    while True:
            try:
                print('Vamos lá, você já sabe as regras')
                escolha_do_jogador = int(input('Escolha sua jogada:\n' \
                '1.Pedra\n' \
                '2.Papel\n' \
                '3.Tesoura\n'))
                if escolha_do_jogador not in (1, 2 ,3):
                    print('Escolha uma opção válida')
                    continue

                return escolha_do_jogador - 1
                
                
            
            except ValueError:
                print('Digite apenas números!')
                continue

def resultado_ppt(escolha_do_jogador):#aqui usamos a escolha da funçao jogo_ppt para determinar o resultado do combate

    global vitorias_ppt, empates_ppt, derrotas_ppt 

    nome_escolha = NOMES[escolha_do_jogador]
    parametro_avaliado = LISTA_JOGADAS[escolha_do_jogador]
        

    jogada_bot = random.randint(0,2)

    escolha_bot = parametro_avaliado[jogada_bot]
    if jogada_bot == 2 :
        print(f'Você jogou {nome_escolha} e eu joguei {escolha_bot} hahaha,quem é o bot aqui?')
        derrotas_ppt += 1
    elif jogada_bot == 1:
        print (f'Você jogou {nome_escolha} e eu joguei {escolha_bot}, dessa vez empatamos!')
        empates_ppt += 1
    else:
        print(f'Você jogou {nome_escolha} e eu joguei {escolha_bot}, parece que perdi dessa vez!')    
        vitorias_ppt += 1
        
def dificuldade_adivinhacao(): #aqui o usuario seleciona o limite, que vai ser a dificuldade dele no jogo de adivinhação
    while True:
        try:
            dificuldade = int(input(
                'Escolha a dificuldade:\n'
                '1. Fácil (1–50)\n'
                '2. Média (1–100)\n'
                '3. Difícil (1–500)\n'
            ))

            if dificuldade not in (1, 2, 3):
                print('Escolha uma dificuldade válida!')
                continue

            return dificuldade
        except ValueError:
            print('Digite apenas números!')

def jogo_adivinhacao(dificuldade):#aqui roda o jogo de avinhação em loop, assim como registra as estatiticas, e computa a derrota caso o numero de tentativas da rodada seja maior que 10
    global tentativas, jogos, erros, tentativas_totais
    if dificuldade == 1:
        limite = 50
    elif dificuldade == 2:
        limite = 100
    else:
        limite = 500

    while True:
        resposta = random.randint(1, limite)
        tentativas = 0
        jogos += 1

        print(f'\n Jogo {jogos} iniciado (1 a {limite})')

        while True:
            try:
                numero = int(input('Digite um número: '))

                if numero < 1 or numero > limite:
                    print(f'Por favor digite um número entre 1 e {limite}!')
                    erros += 1
                    continue

                tentativas += 1

                if numero == resposta:
                    print(f'Parabéns! Você acertou em {tentativas} tentativas!')
                    tentativas_totais += tentativas
                    break
                elif numero > resposta:
                    print('Menor que isso')
                else:
                    print('Maior que isso')

                print(f'Tentativas válidas: {tentativas}')

                if tentativas >= 10:
                    print('Você atingiu o limite de tentativas')
                    print(f'O número correto era {resposta}')
                    tentativas_totais += tentativas
                    break

            except ValueError:
                erros += 1
                print('Digite apenas números!')

        repetir = input('Deseja jogar novamente? (s/n): ')
        jogar_novamente = repetir.lower() in ['s', 'sim']

        if not jogar_novamente:
            break

def loop_ppt(): #esse e o loop do pedra papel tesousa  
    while True:
        escolha_do_jogador = jogo_ppt()
        resultado_ppt(escolha_do_jogador)
        
        print(f'Vitórias:{vitorias_ppt}\nDerrotas:{derrotas_ppt}\nEmpates:{empates_ppt}\n')
        replay = input('Deseja jogar novamente?')
        if replay.lower() in ['s','sim']:
            continue
        break

def loop_adivinhacao():#e esse e o loop da adivinhação
    dificuldade = dificuldade_adivinhacao()
    jogo_adivinhacao(dificuldade)     

def placar_total():#aqui e onde estao registrados os scores, estou pensando em alterar os scores para uma lista dps
    while True:
        placar_escolhido = input('Qual placar você deseja ver?\n' \
        'Pedra, papel e tesoura\n'
        'Adivinhação\n').lower()
        
        if placar_escolhido in ('pedra','pedr','p','pe','pedra, papel e tesoura'):
            if vitorias_ppt + derrotas_ppt + empates_ppt == 0:
                print('Você ainda não jogou nenhuma rodado, jogue antes de voltar aqui!')
                break
            print(f'Vitórias:{vitorias_ppt},Empates:{empates_ppt}, Derrotas:{derrotas_ppt}')
            porcentagem_ppt =(vitorias_ppt / (vitorias_ppt + derrotas_ppt + empates_ppt) * 100) ##nessa linha ia dividir um pelo outro mas se alguma info fosse 0 iam crashar
            print(f'Essa foi sua porcentagem de vitórias total:{porcentagem_ppt:.2f}')

        elif placar_escolhido in ('adivinhação', 'adivinhacao', 'adv', 'advi'):
            if jogos == 0 :
                print('Você ainda não tentou adivinhar nada')
                break
            print(f'Jogos:{jogos},Tentativas totais: {tentativas_totais}, e um total absurdo de {erros} erros!')
            porcentagem_adv = (erros / tentativas_totais) * 100
            print(f'Essa é a sua porcentagem total de erros: {porcentagem_adv:.2f}')
        
        outro_placar = input('Deseja ver outro placar?').lower
        if outro_placar in ('s','ss','sim'):
            continue
        break

def main():#programa principal
    while True:
        jogo_selecionado = menu_geral()
        if jogo_selecionado == 1:
            loop_ppt()
        elif jogo_selecionado == 2:
            loop_adivinhacao()
        elif jogo_selecionado == 4:
            placar_total()
        elif jogo_selecionado == 5: 
            break
if '__name__' == '__main__':
    main()

##apos o codigo finalizado
##alterei e coloquei o ponto 2f para n mostrar dizima nas porcentagens

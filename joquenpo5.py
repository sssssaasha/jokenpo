from random import randint
import getpass
print("--- Menu Jokenpô ---")
print("1 - humano x humano")
print("2 - humano x computador")
print("3 - computador x computador")
print("4 - sair do jogo")
menu = int(input("Escolha o modo de jogo: "))

while menu <= 3 and menu != 4:

    round1 = 0
    placarUm = 0
    placarDois = 0
    while menu == 1:
        round1 += 1
        print(f'--- Round {round1} ---')
        if menu == 1:
            jogadorUm = getpass.getpass("Jogador um escolha pedra, papel ou tesoura: ")
            jogadorDois = getpass.getpass("Jogador dois escolha pedra, papel ou tesoura: ")
            print("j1: ", jogadorUm, "\nj2: ", jogadorDois)
            if (jogadorUm == 'pedra' or jogadorUm == 'papel' or jogadorUm == 'tesoura') and (jogadorDois == 'pedra' or jogadorDois == 'papel' or jogadorDois == 'tesoura'):
                if jogadorUm == 'tesoura' and jogadorDois == 'papel':
                    placarUm = placarUm + 1
                elif jogadorUm == 'tesoura' and jogadorDois == 'pedra':
                    placarDois = placarDois + 1
                elif jogadorUm == 'pedra' and jogadorDois == 'tesoura':
                    placarUm = placarUm + 1
                elif jogadorUm == 'pedra' and jogadorDois == 'papel':
                    placarDois = placarDois + 1
                elif jogadorUm == 'papel' and jogadorDois == 'tesoura':
                    placarDois = placarDois + 1
                elif jogadorUm == 'papel' and jogadorDois == 'pedra':
                    placarUm = placarUm + 1
                else:
                    print("Empate")
        print("--- Placar ---")
        print(f' {placarUm} vs {placarDois}')
        menu = int(input('Se gostaria de continuar digite 1, se não, digite 5: '))
        if menu != 1 and menu != 2 and menu != 3 and menu != 4:
            print("--- Menu Jokenpô ---")
            print("1 - humano x humano")
            print("2 - humano x computador")
            print("3 - computador x computador")
            print("4 - sair do jogo")
            menu = int(input("Escolha o modo de jogo: "))

    round2 = 0
    placarTeste1 = 0
    placarComputador1 = 0
    while menu == 2:
        if menu == 2:
            round2 += 1
            print(f'--- Round {round2} ---')
            jogadorUm = input("Jogador escolha pedra, papel ou tesoura: ")
            itens = ('pedra', 'papel', 'tesoura')
            computador = randint(0,2)
            print(itens[computador])
            if (jogadorUm == 'pedra' or jogadorUm == 'papel' or jogadorUm == 'tesoura'):
                if jogadorUm == 'tesoura' and itens[computador] == 'papel':
                    placarTeste1 = placarTeste1 + 1
                elif jogadorUm == 'tesoura' and itens[computador] == 'pedra':
                    placarComputador = placarComputador1 + 1
                elif jogadorUm == 'pedra' and itens[computador] == 'tesoura':
                    placarTeste1 = placarTeste1 + 1
                elif jogadorUm == 'pedra' and itens[computador] == 'papel':
                    placarComputador = placarComputador1 + 1
                elif jogadorUm == 'papel' and itens[computador] == 'tesoura':
                    placarComputador = placarComputador1 + 1
                elif jogadorUm == 'papel' and itens[computador] == 'pedra':
                    placarTeste1 = placarTeste1 + 1
                else:
                    print("Empate")
            print("--- Placar ---")
            print(f' {placarTeste1} vs {placarComputador1}')
            menu = int(input('Se gostaria de continuar digite 2, se não, digite 5: '))
            if menu != 1 and menu != 2 and menu != 3 and menu != 4:
                print("--- Menu Jokenpô ---")
                print("1 - humano x humano")
                print("2 - humano x computador")
                print("3 - computador x computador")
                print("4 - sair do jogo")
                menu = int(input("Escolha o modo de jogo: "))

    round3 = 0
    placarTeste2 = 0
    placarComputador2 = 0
    while menu == 3:
        round3 += 1
        print(f'--- Round {round3} ---')
        if menu == 3:
            itens = ('pedra','papel','tesoura')
            computadorUm = randint(0,2)
            computadorDois = randint(0,2)
            print(itens[computadorUm])
            print(itens[computadorDois])

            if itens[computadorUm] == 'tesoura' and itens[computadorDois] == 'papel':
                placarTeste2 = placarTeste2 + 1
            elif itens[computadorUm] == 'tesoura' and itens[computadorDois] == 'pedra':
                placarComputador2 = placarComputador2 + 1
            elif itens[computadorUm] == 'pedra' and itens[computadorDois] == 'tesoura':
                placarTeste2 = placarTeste2 + 1
            elif itens[computadorUm] == 'pedra' and itens[computadorDois] == 'papel':
                placarComputador2 = placarComputador2 + 1
            elif itens[computadorUm] == 'papel' and itens[computadorDois] == 'tesoura':
                placarComputador2 = placarComputador2 + 1
            elif itens[computadorUm] == 'papel' and itens[computadorDois] == 'pedra':
                placarTeste2 = placarTeste2 + 1
            else:
                print("Empate")
        print("--- Placar ---")
        print(f' {placarTeste2} vs {placarComputador2}')
        menu = int(input('Se gostaria de continuar digite 3, se não, digite 5: '))
        if menu != 1 and menu != 2 and menu != 3 and menu != 4:
            print("--- Menu Jokenpô ---")
            print("1 - humano x humano")
            print("2 - humano x computador")
            print("3 - computador x computador")
            print("4 - sair do jogo")
            menu = int(input("Escolha o modo de jogo: "))


    if menu == 4:
        print("Encerrando o jokenpô...")
        print("Muito obrigada, ")
        print("Alex Menegatti Secco, ")
        print("Ana Flávia Martins dos Santos, ")
        print("Isabella Vanderlinde Berkembrock, ")
        print("Mariana de Castro, ")
        print("Nicole Pereira Guarnieri!")

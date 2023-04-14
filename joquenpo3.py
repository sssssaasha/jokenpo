from random import randint
print("--- Menu Jokenpô ---")
print("1 - humano x humano")
print("2 - humano x computador")
print("3 - computador x computador")
print("4 - sair do jogo")
menu = int(input("Escolha o modo de jogo: "))
placarUm = 0
placarDois = 0
placarTeste = 0
placarComputador = 0
round = 0

while menu <=3 and menu!= 4:
    while menu == 1:

        if menu == 1:
            round += 1
            print(f'--- Round {round} ---')
            jogadorUm = input("Jogador um escolha pedra, papel ou tesoura: ")
            jogadorDois = input("Jogador dois escolha pedra, papel ou tesoura: ")

            if (jogadorUm == 'pedra' or jogadorUm == 'papel' or jogadorUm == 'tesoura') and (jogadorDois == 'pedra' or jogadorDois == 'papel' or jogadorDois == 'papel'):
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

    while menu == 2:

        if menu == 2:
            round += 1
            print(f'--- Round {round} ---')
            jogadorUm = input("Jogador escolha pedra, papel ou tesoura: ")
            itens = ('pedra', 'papel', 'tesoura')
            computador = randint(0,2)
            print(itens[computador])
            if (jogadorUm == 'pedra' or jogadorUm == 'papel' or jogadorUm == 'tesoura'):
                if jogadorUm == 'tesoura' and itens[computador] == 'papel':
                    placarTeste = placarTeste + 1
                elif jogadorUm == 'tesoura' and itens[computador] == 'pedra':
                    placarComputador = placarComputador + 1
                elif jogadorUm == 'pedra' and itens[computador] == 'tesoura':
                    placarTeste = placarTeste + 1
                elif jogadorUm == 'pedra' and itens[computador] == 'papel':
                    placarComputador = placarComputador + 1
                elif jogadorUm == 'papel' and itens[computador] == 'tesoura':
                    placarComputador = placarComputador + 1
                elif jogadorUm == 'papel' and itens[computador] == 'pedra':
                    placarTeste = placarTeste + 1
                else:
                    print("Empate")
            print("--- Placar ---")
            print(f' {placarTeste} vs {placarComputador}')
            menu = int(input('Se gostaria de continuar digite 2, se não, digite 5: '))
            if menu != 1 and menu != 2 and menu != 3 and menu != 4:
                print("--- Menu Jokenpô ---")
                print("1 - humano x humano")
                print("2 - humano x computador")
                print("3 - computador x computador")
                print("4 - sair do jogo")
                menu = int(input("Escolha o modo de jogo: "))


    while menu == 3:

        if menu == 3:
            round += 1
            print(f'--- Round {round} ---')
            itens = ('pedra','papel','tesoura')
            computadorUm = randint(0,2)
            computadorDois = randint(0,2)
            print(itens[computadorUm])
            print(itens[computadorDois])

            if itens[computadorUm] == 'tesoura' and itens[computadorDois] == 'papel':
                placarTeste = placarTeste + 1
            elif itens[computadorUm] == 'tesoura' and itens[computadorDois] == 'pedra':
                placarComputador = placarComputador + 1
            elif itens[computadorUm] == 'pedra' and itens[computadorDois] == 'tesoura':
                placarTeste = placarTeste + 1
            elif itens[computadorUm] == 'pedra' and itens[computadorDois] == 'papel':
                placarComputador = placarComputador + 1
            elif itens[computadorUm] == 'papel' and itens[computadorDois] == 'tesoura':
                placarComputador = placarComputador + 1
            elif itens[computadorUm] == 'papel' and itens[computadorDois] == 'pedra':
                placarTeste = placarTeste + 1
            else:
                print("Empate")
        print("--- Placar ---")
        print(f' {placarTeste} vs {placarComputador}')
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


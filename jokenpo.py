import random
while True:

    # Menu

    modo = int(input("Digite 1 para PVP; Digite 2 para PVE; Digite 3 para EVE: "))
    q = 0  # placar do jogador 1
    w = 0  # placar do jogador 2
    nome1 = input("Digite nome do jogador1: ")
    nome2 = input("Digite nome do jogador2: ")
    AIchoise = ["pedra", "papel", "tesoura"]
    while modo == 1:

        # Escolher a jogada

        jogador1 = input("Digite a sua escolha "+str(nome1)+": ")
        jogador2 = input("Digite a sua escolha "+str(nome2)+": ")

        # Mostrando a jogada de cada um

        print("O "+str(nome1)+" tirou: "+str(jogador1))
        print("O "+str(nome2)+" tirou: "+str(jogador2))

        # Mostrar o resultado e escolher se quer continuar ou sair

        if (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "tesoura" and jogador2 == "papel") or (jogador1 == "papel" and jogador2 == "pedra"):
            q = q+1
            print("Parabéns "+str(nome1)+",você ganhou!!!")
            con = input("Digite c para continuar ou s para sair: ")
            if con == "c":
                continue
            if con == "s":
                print("Placar"+str(q)+":"+str(w))
                print("Boa partida "+str(nome1)+","+str(nome2))
                break
        if (jogador2 == "pedra" and jogador1 == "tesoura") or (jogador2 == "tesoura" and jogador1 == "papel") or (jogador2 == "papel" and jogador1 == "pedra"):
            w = w+1
            print("Parabéns "+str(nome2)+",você ganhou!!!")
            con = input("Digite c para continuar ou s para sair: ")
            if con == "c":
                continue
            if con == "s":
                print("Placar" + str(q) + ":" + str(w))
                print("Boa partida "+str(nome1)+","+str(nome2))
                break
        if jogador1 == jogador2:
            print("Empate")
            con = input("Digite c para continuar ou s para sair: ")
            if con == "c":
                continue
            if con == "s":
                print("Placar" + str(q) + ":" + str(w))
                print("Boa partida " + str(nome1) + "," + str(nome2))
                break
    while modo == 2:

        # Escolher a jogada

        jogador = input("Digite a sua escolha: ")
        computador = random.choice(AIchoise)

        # Mostrando a jogada de cada um

        print("O "+str(nome1)+" tirou: " + str(jogador))
        print("O AI tirou: " + str(computador))

        # Mostrar o resultado e escolher se quer continuar ou sair

        if (jogador == "pedra" and computador == "tesoura") or (jogador == "tesoura" and computador == "papel") or (jogador == "papel" and computador == "pedra"):
            q = q+1
            print("Parabéns "+str(nome1)+" , você ganhou!!!")
            con = input("Digite c para continuar ou s para sair: ")
            if con == "c":
                continue
            if con == "s":
                print("Placar"+str(q)+":"+str(w))
                print("Boa partida " + str(nome1) + "," + str(nome2))
                break
        if (computador == "pedra" and jogador == "tesoura") or (computador == "tesoura" and jogador == "papel") or (computador == "papel" and jogador == "pedra"):
            w = w+1
            print("Parabéns "+str(nome2)+" , você ganhou!!!")
            con = input("Digite c para continuar ou s para sair: ")
            if con == "c":
                continue
            if con == "s":
                print("Placar" + str(q) + ":" + str(w))
                print("Boa partida " + str(nome1) + "," + str(nome2))
                break
        if jogador == computador:
            print("Empate")
            con = input("Digite c para continuar ou s para sair: ")
            if con == "c":
                continue
            if con == "s":
                print("Placar" + str(q) + ":" + str(w))
                print("Boa partida " + str(nome1) + "," + str(nome2))
                break
    while modo == 3:

        # Escolher a jogada

        computador1 = random.choice(AIchoise)
        computador2 = random.choice(AIchoise)

        # Mostrando a jogada de cada um

        print("O AI1 tirou: " + str(computador1))
        print("O AI2 tirou: " + str(computador2))

        # Mostrar o resultado e escolher se quer continuar ou sair

        if (computador1 == "pedra" and computador2 == "tesoura") or (computador1 == "tesoura" and computador2 == "papel") or (computador1 == "papel" and computador2 == "pedra"):
            q = q+1
            print("Parabéns "+str(nome1)+" , você ganhou!!!")
            con = input("Digite c para continuar ou s para sair: ")
            if con == "c":
                continue
            if con == "s":
                print("Placar"+str(q)+":"+str(w))
                print("Boa partida " + str(nome1) + "," + str(nome2))
                break
        if (computador2 == "pedra" and computador1 == "tesoura") or (computador2 == "tesoura" and computador1 == "papel") or (computador2 == "papel" and computador1 == "pedra"):
            w = w+1
            print("Parabéns "+str(nome2)+" , você ganhou!!!")
            con = input("Digite c para continuar ou s para sair: ")
            if con == "c":
                continue
            if con == "s":
                print("Placar" + str(q) + ":" + str(w))
                print("Boa partida " + str(nome1) + "," + str(nome2))
                break
        if computador1 == computador2:
            print("Empate")
            con = input("Digite c para continuar ou s para sair: ")
            if con == "c":
                continue
            if con == "s":
                print("Placar" + str(q) + ":" + str(w))
                print("Boa partida " + str(nome1) + "," + str(nome2))
                break
                
from random import choice  # fará com que a maquina escolha 1 opção aleatoria

jogador_virotias = 0  # ira marcar as vitorias do jogador começando por 0
maq_vitorias = 0  # ira marcar as vitorias da maquina começando por 0


def Opcao_Jogador():
    # ira dar opção para o jogador escolher
    esc_jogador = input("Escolha Pedra, Papel, Ou Tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "Pedra":
        return esc_jogador

    elif esc_jogador == "Papel":
        return esc_jogador

    elif esc_jogador == "Tesoura":
        return esc_jogador

    else:
        print("opção inválida, escolha Pedra, Papel, Ou Tesoura ")
        Opcao_Jogador()
# ira fazer o jogo retornar ou continuar de acordo com a escolha


def Opcao_Maquina():
    # opções que a maquina pode escolher
    esc_maquina = choice(["Pedra"]),
    esc_maquina = choice(["Papel"]),
    esc_maquina = choice(["Tesoura"])
    return esc_maquina


while True:

    print("-"*30)  # imprimir com espaçamento
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maquina()

    print("-"*30)
    print(f"Vitorias do jogador: {jogador_virotias}")
    print(f"Vitorias da maquina: {maq_vitorias}")
    print("-"*30)

    if (esc_jogador == "Pedra") and (esc_maquina == "Tesoura") \
            or (esc_jogador == "Papel") and (esc_maquina == "Pedra") \
            or (esc_jogador == "Tesoura") and (esc_maquina == "Papel"):

        print(f"jogador{esc_jogador} maquina {esc_maquina}"
              "Resultado:Você Ganhou, Parabéns! ")
        print("Voce Ganhou, Parabéns!")
        jogador_virotias += 1

    elif esc_jogador == esc_maquina:
        print(f"jogador{esc_jogador} maquina {esc_maquina}"
              "Resultado:Deu Empate! ")
        print("Deu Empate! ")

    else:
        print(f"jogador{esc_jogador} maquina {esc_maquina}"
              "Resultado:Você Ganhou, Parabéns! ")
        print("Voce Perdeu!")
        maq_vitorias += 1

    print("-"*30)
    esc_jogador = input("Deseja Jogar Novamente? ")
    if esc_jogador in ["Sim", "sim", "SIM", "s", "S"]:
        pass
    elif esc_jogador in ["Não", "não", "NÃO", "Nao", "nao", "NAO", "n", "N"]:
        break
    else:
        break
    # da opção para o jogador de continuar ou não, parando ou recomeçar o jogo

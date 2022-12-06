palpite = 1
numero = 9

while True:  # executa sem verificação de true ou false
    print("adivinhe o numero")  # imprimi o que sera perguntando
    palpite = int(input())  # confirma
    if palpite == numero:  # se estiver correto, imprimi o seguinte texto
        print("Você Acertou Parabéns!")
        break  # interrompe o codigo, caso acertar
    else:  # se nao estiver correto, imprimi o seguinte texto, e inicia novamente o codigo
        print("Você errou tente novamente.")

else:  # para o desenvolvedor ver, caso tenha algum erro
    print("erro na aplicação")
    print(bool(palpite))

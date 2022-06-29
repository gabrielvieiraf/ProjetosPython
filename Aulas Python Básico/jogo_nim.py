def usuario_escolhe_jogada(n, m):
    jogada_usuario = True

    while jogada_usuario:
        qnt_pecas_removidas = int(input("Quantas peças você vai tirar? "))
        conditions = qnt_pecas_removidas < 1 or qnt_pecas_removidas > m or qnt_pecas_removidas > n
            
        if conditions:
            jogada_usuario = True
            print("\nOops! Jogada inválida! Tente de novo.\n")
        else: 
            jogada_usuario = False
            
    return qnt_pecas_removidas


def computador_escolhe_jogada(n, m):
    qnt_pecas_removidas = n if n <= m else m if n % (m + 1) == 0 else n % (m + 1)
    return qnt_pecas_removidas


def partida():
    n, m = int(input("Quantas peças? ")), int(input("Limite de peças por jogada? "))     
    vez_pc = False
    
    print( "\nVocê começa!\n" if n % (m + 1) == 0 else "\nComputador começa!\n")
    
    if n % (m + 1) != 0:
        vez_pc = True

    while n > 0:
        if vez_pc:
            qnt_pc_remove = computador_escolhe_jogada(n, m)
            n -= qnt_pc_remove
            print("O computador tirou uma peça." if qnt_pc_remove == 1 else f"O computador tirou {qnt_pc_remove} peças", end='')
            vez_pc = False
        else:
            qnt_usuario_remove = usuario_escolhe_jogada(n, m)
            n -= qnt_usuario_remove
            print("\nVocê tirou uma peça." if qnt_usuario_remove == 1 else f"\nVocê tirou {qnt_usuario_remove} peças")
            vez_pc = True

        print("Agora resta apenas uma peça no tabuleiro.\n" if n == 1 else 
            f"Agora restam {n} peças no tabuleiro.\n" if n != 0 else '')

    
    print("Fim do jogo! Você Ganhou!\n" if vez_pc else "Fim do jogo! O computador Ganhou!\n")
    return 1 if vez_pc else 0


def campeonato():
    n_rodada = 1
    placar_usuario = 0
    placar_pc = 0
    
    while n_rodada <= 3:
        print(f"**** Rodada {n_rodada} ****\n")
        vencedor = partida()
        n_rodada += 1
        placar_usuario += 1 if vencedor == 1 else 0
        placar_pc += 1 if vencedor== 0 else 0
    
    print("**** Final do campeonato! ****") 
    print(f"Placar: Você {placar_usuario} X {placar_pc} Computador")
    return True


print("Bem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato", end='')
opcao = int(input(" "))

if opcao == 1:
    print("Voce escolheu uma partida!\n")
    partida()
    print("**** Partida Isolada ****\n")
else:
    print("\nVoce escolheu um campeonato!\n")
    campeonato()
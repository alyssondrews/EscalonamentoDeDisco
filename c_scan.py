class CSCAN():
    calculo = 0
    n_elementos = int(input("Insira aqui o número de elementos:\n"))
    pos_inicial = int(input("Insira aqui a posição inicial:\n"))
    lista = [int(input("Insira o elemento que deseja:\n")) for i in range(n_elementos)]
    posicao = pos_inicial
    comeco = 0
    final = 199

    print("A ordem dos elementos é:\n", pos_inicial, end='')
    if (pos_inicial <100):
        for i in range (posicao, comeco-1, -1):
            if i in lista:
                calculo = calculo + abs(posicao-i)
                posicao = i
                print(" ", i, end='')
                lista.remove(i)
        calculo = calculo + abs(posicao - comeco)
        posicao = final
        print(" ", comeco, end='')
        print(" ", final, end='')
        for i in range(final, pos_inicial+1, -1):
            if i in lista:
                calculo = calculo + abs(posicao - i)
                posicao = i
                print(" ", i, end='')
                lista.remove(i)
    else:
        for i in range(posicao, comeco +1):
            if i in lista:
                tempo = tempo + abs(posicao - i)
                posicao = i
                print(" ", i, end = '')
                lista.remove(i)
        calculo = calculo + abs(posicao - final)
        posicao = comeco
        print(" ", final, end='')
        for i in range(comeco, pos_inicial+1):
            if i in lista:
                calculo = calculo + abs(posicao - i)
                posicao = i
                print(" ", i, end='')
                lista.remove(i)

    print("\nO resultado do calculo é:\n", calculo)
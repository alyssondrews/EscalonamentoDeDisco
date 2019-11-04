class CLOOK():
    calculo = 0
    n_elementos = int(input("Insira aqui o número de elementos:\n"))
    pos_inicial = int(input("Insira aqui a posição inicial:\n"))
    lista = [int(input("Insira o elemento que deseja:\n")) for i in range(n_elementos)]
    posicao = pos_inicial
    comeco = min(lista)
    final = max(lista)
    print("A ordem dos elementos é:\n",pos_inicial, end='')
    if((abs(pos_inicial-comeco))<(abs(pos_inicial-final))):
        for i in range(posicao, comeco -1, -1):
            if i in lista:
                calculo+= abs(posicao-i)
                posicao = i
                print(" ", i, end='')
                lista.remove(i)
        calculo += abs(posicao-comeco)
        posicao = final
        print(" ", comeco, end='')
        print(" ", final, end='')
        for i in range(final, pos_inicial+1,-1):
            if i in lista:
                calculo += abs(posicao-i)
                posicao = i
                print(" ", i, end='')
                lista.remove(i)
    else:
        for i in range(posicao, final +1):
            if i in lista:
                calculo += abs(posicao-i)
                posicao = i
                print(" ", i, end='')
                lista.remove(i)
        calculo += abs(posicao - final)
        posicao = comeco
        print(" ", final, end='')
        print(" ", comeco, end='')
        for i in range(comeco, pos_inicial+1):
            if i in lista:
                calculo += abs(posicao - i)
                posicao = i
                print(" ", i, end='')
                lista.remove(i)
    print("\nO resultado do cálculo é:\n",calculo)
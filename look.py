class LOOK():
    calculo = 0
    n_elementos = int(input("Insira aqui o número de elementos:\n"))
    pos_inicial = int(input("Insira aqui a posição inicial:\n"))
    lista = [int(input("Insira o elemento que deseja:\n")) for i in range(n_elementos)]
    posicao = pos_inicial
    comeco = min(lista)
    final = max(lista)
    print("A ordem dos elementos é\n",pos_inicial, end='')
    if((abs(pos_inicial-comeco))<(abs(pos_inicial-final))):
        for i in range(posicao,comeco - 1, -1):
            if i in lista:
                calculo = calculo + abs(posicao-i)
                posicao = i
                print(" ",i,end='')
                lista.remove(i)
        calculo = calculo + abs(posicao-comeco)
        posicao = comeco
        print(" ",comeco, end='')
        for i in range(posicao, final+1):
            if i in lista:
                calculo+= abs(posicao-i)
                posicao = i
                print(" ", i, end='')
                lista.remove(i)
    else:
        for i in range(posicao, final+1):
            if i in lista:
                calculo+= abs(posicao-i)
                posicao = i
                print(" ", i, end='')
                lista.remove(i)
        calculo += abs(posicao - final)
        posicao = final
        print(" ", final, end='')
        for i in range(posicao, comeco-1,-1):
            if i in lista:
                calculo += abs(posicao-i)
                posicao = i
                print(" ", i, end='')
                lista.remove()
    print("\nO resultado do calculo é:\n", calculo)
                

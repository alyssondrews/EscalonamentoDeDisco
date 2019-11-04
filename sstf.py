from heapq import *

class SSTF():
    n_elementos = int(input("Insira aqui o número de elementos:\n"))
    pos_inicial = int(input("Insira aqui a posição inicial:\n"))
    lista = [int(input("Insira o elemento que deseja:\n")) for i in range(n_elementos)]
    r = 0
    calculo = 0
    posicao = pos_inicial
    heap = []
    n = len(lista)
    print("A ordem dos elementos é:\n",pos_inicial, end='')
    while len(lista) > 0:
        for r in lista:
            heappush(heap, [abs(posicao-r),r])
        x = heappop(heap)[1]
        calculo = calculo + abs(posicao-x)
        print(" ",x, end='')
        posicao = x
        lista.remove(x)
        heap = []
    print("\nO resultado do calculo é:\n", calculo)
    
    
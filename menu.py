import os
from heapq import *

def fcfs():
    n_elementos = int(input("Insira aqui o número de elementos:\n"))
    pos_inicial = int(input("Insira aqui a posição inicial:\n"))
    lista = [int(input("Insira o elemento que deseja:\n")) for i in range(n_elementos)]
    calculo = 0
    calculo = calculo + abs(pos_inicial - lista[0])
    for i in range(1, n_elementos):
        calculo = calculo + abs(lista[i] - lista[i-1])
        
    print("O resultado do cálculo é:\n", calculo)
    print("A ordem dos elementos é:\n", pos_inicial, lista)

def sstf():
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

def scan():
    calculo = 0
    n_elementos = int(input("Insira aqui o número de elementos:\n"))
    pos_inicial = int(input("Insira aqui a posição inicial:\n"))
    lista = [int(input("Insira o elemento que deseja:\n")) for i in range(n_elementos)]
    posicao = pos_inicial
    comeco = 0
    final = 199
    print("A ordem dos elementos é:\n", pos_inicial, end = '')
    if(posicao < 100):
        for i in range(posicao, comeco -1, -1):
            if i in lista:
                calculo = calculo + abs(posicao - i)
                print(" ",i,end='')
                lista.remove(i)
        calculo = calculo + abs(posicao-comeco)
        posicao = comeco
        print(" ", comeco, end='')
        for i in range(posicao,final+1):
            if i in lista:
                calculo = calculo + abs(posicao-i)
                posicao = i
                print(" ", i, end='')
                lista.remove(i)
    else:
        for i in range(posicao, final+1):
            if i in lista:
                calculo = calculo + abs(posicao - i)
                posicao = i
                print(" ", i, end='')
                lista.remove(i)
        calculo = calculo + abs(posicao - final)
        posicao = final
        print(" ", final, end='')
        for i in range (posicao, comeco-1,-1):
            if i in lista:
                calculo = calculo + abs(posicao - i)
                posicao = i
                print(" ", i, end='')
    print("\nO resultado do calculo é:\n", calculo)

def cscan():
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
def look():
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
                
def clook():
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

def limpa_tela():
    os.system('cls') or None


limpa_tela()
print("#####    ESCALONAMENTO DE E/S    #####")
opcao = int(input("Insira o método de escalonamento desejado:\n1: FCFS\n2: SSTF\n3: SCAN\n4: C-SCAN\n5: LOOK\n5: C-LOOK\n"))
if opcao == 1:
    fcfs()
if opcao == 2:
    sstf()
if opcao == 3:
    scan()
if opcao == 4:
    cscan()
if opcao == 5:
    look()
if opcao == 6:
    clook()
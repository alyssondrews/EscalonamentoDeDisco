class FCFS():
    n_elementos = int(input("Insira aqui o número de elementos:\n"))
    pos_inicial = int(input("Insira aqui a posição inicial:\n"))
    lista = [int(input("Insira o elemento que deseja:\n")) for i in range(n_elementos)]
    calculo = 0
    calculo = calculo + abs(pos_inicial - lista[0])
    for i in range(1, n_elementos):
        calculo = calculo + abs(lista[i] - lista[i-1])
        
    print("O resultado do cálculo é:\n", calculo)
    print("A ordem dos elementos é:\n", pos_inicial, lista)


from metodo import *
lista = []
K = int(input('Quantos clusters: '))
igual = True
clus = []
while igual:
    op = menu()
    if op == 1:
        cadastrar(lista)
    elif op == 2:
        clus = k_means(lista, K)
    elif op == 3:
        imprimir(clus)
    elif op == 4:
        grafico(clus)
    elif op == 0:
      igual = False

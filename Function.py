
import random
import math
import matplotlib.pyplot as plt


def menu():
    print('\n------------------- Mini Menu -------------------\n')
    print('1.Ler Arquivos')
    print('2.Calcular distâncias')
    print('3.Printar clusters')
    print('4.Plotar gráfico')
    print('\n--------------------------------------------------\n')
    op = int(input('Qual opção será escolhida: '))
    return op


def k_means(points, k):
    # Inicializando os centróides aleatoriamente
    centroids = random.sample(points, k)

    while True:
        # Inicializando os clusters vazios
        clusters = [[] for _ in range(k)]

        # Atribuindo cada ponto ao cluster mais próximo
        for point in points:
            distances = [math.dist(point, centroid) for centroid in centroids]
            nearest_cluster = distances.index(min(distances))
            clusters[nearest_cluster].append(point)

        # Calculando os novos centróides
        new_centroids = [list(map(lambda x: sum(x) / len(x), zip(*cluster))) for cluster in clusters]

        # Se os centróides não mudaram, retornar os clusters
        if new_centroids == centroids:
            return clusters

        centroids = new_centroids


def cadastrar(lista):
    x = []
    y = []
    with open('ArquivoX.txt', 'r') as arquivo:
        for linha in arquivo:
            x.append(linha)
    with open('ArquivoY.txt', 'r') as arquivo:
        for linha in arquivo:
            y.append(linha)

    for i in range(len(x)):
        tupla = (int(x[i]), int(y[i]))
        lista.append(tupla)


def imprimir(clus):
    for i, cluster in enumerate(clus):
        print(f"Cluster {i}: {cluster}")


def grafico(clus):
    j = 0
    color = ['red', 'blue', 'green', 'yellow', 'black', 'pink', 'orange']
    for t in clus:
        x = []
        y = []
        tamanho = len(t)
        for i in range(tamanho):
            x.append(t[i][0])
            y.append(t[i][1])
        plt.scatter(x, y, color=color[j], label=f'Cluster {j}')
        j = j + 1
    plt.title('Scatter Plot com Categorias')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend()
    plt.show()

n = 7
matriz_length = n ** 2
matriz = []
index = 0

for mult in range(n):
    matriz.append([])

for num in range(matriz_length):
    if ((num + 1) % n) == 0:
        matriz[index].append(num + 1)
        index += 1

        continue

    matriz[index].append(num + 1)

for arr in matriz:
    if (matriz.index(arr) % 2) != 0:
        arr.reverse()

for row in zip(*matriz):
    print(*row)

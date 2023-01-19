import random

n = 50 # zadaję liczbę wierzchołków
moja_lista = []
number_of_element = 0
for i in range(n):
    moja_lista.append([])

while number_of_element < n:
    x = random.randint(1, 99)
    y = random.randint(1, 99)

    if not [x, y] in moja_lista:
        moja_lista[number_of_element].append(x)
        moja_lista[number_of_element].append(y)
        number_of_element = number_of_element + 1



file = "../App/generate_graph_2.txt"
f = open(file, "w")
for i in range(n):
    line = ' '.join([str(moja_lista[i][0]), str(moja_lista[i][1])])
    f.write(line)
    if i != n-1:
        f.write("\n")

f.close()

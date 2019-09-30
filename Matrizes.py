#Criando uma lista repleta de zeros
#inteiros
'''linhas = 3
colunas = 4
M = []
for i in range(linhas):
    M.append([0] * colunas)
print(M)'''

#Strings
'''linhas = 3
colunas = 4
M = []
for i in range(linhas):
    M.append([""] * colunas)
print(M)'''

#Vazio
'''linhas = 3
colunas = 4
a = []
for i in range(linhas):
    a.append([] * colunas)
print(a)'''

#Processando uma matriz
'''Suponha que você receba uma matriz quadrada (uma matriz de n linhas e
n colunas). E suponha que você tenha que definir elementos da diagonal 
principal igual a 1 (isto é, esses elementos a[i][j] para os quais i==j),
definir elementos acima da diagonal igual a 0 e definir elementos abaixo
dessa diagonal igual a 2. Ou seja, você precisa produzir tal matriz
(exemplo para n==4 ): 

1 0 0 0
2 1 0 0
2 2 1 0
2 2 2 1
'''
#Criando matriz
#linhas = colunas
linhas = 4
a = []
for i in range(linhas):
    a.append([0] * linhas)

for i in range(linhas):
    for j in range(linhas):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1

print(a)

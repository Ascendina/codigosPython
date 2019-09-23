##Comandos com lista
#lista vazia
#num = []
#num = [1,2,3,4,5,6]
nomes = ["Carlos", "Carol", "Alberto", "Luiz"]
mistura = [1,2,3, "Caio", "Joana"]

#print(num[3])

#quantidade de elementos da lista
#print(len(num))

#Adicionando elemento sem posição
#num.append(10)
#print(num)

#Adicionando elemento com posição
#num.insert(3,40)
#print(num)

#remover elemento da lista
#num.remove(40)
#print(num)

#Remover um elemento da lista com posição
#num.pop(3)
#print(num)

#Remover um elemento da lista com posição
#del(num[3])
#print(num)

#Ordenar uma lista
#print(sorted(num))

#Lista em reverso
#print(list(reversed(num)))

#Operações com lista
#print(sum(num))
#print(max(num))
#print(min(num))

#Quantidade de repetições do elemento
#print(num.count(4))

#Posição do elemento na lista
#print(num.index(5))

#Limpar a lista
#num.clear()
#print(num)

#Preencher uma lista com valores do usuário
num = []
for i in range(0,10):
    num.append(int(input("Digite um número: \n")))

print("Lista completa: " + str(num))
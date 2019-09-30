#Arquivo de leitura

##Iniciando a leitura do arquivo
'''myfile = open("./data/beer.txt", "r+")
file = myfile.readline()


while (file != ""):
    file = myfile.readline()
    print(file)


myfile.close()'''

#Para a leitura de várias linhas
'''myfile = open("./data/sun.txt", "r+")
file = myfile.readlines()

for i in range(len(file)):
    print(file[i])


myfile.close()'''

#Para a escrita de um arquivo (o arquivo já deve existir)
myfile = open("./data/escrita.txt", "w")

s = ["O ", "rato ", "roeu ", " a", " roupa", " do", " rei", " de", " Roma"]

myfile.write("Teste" + "\n")
myfile.writelines(s)


myfile.close()
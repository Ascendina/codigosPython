#Funcoes
#Um trecho de código que é muito utilizado no programa
#pode ser reorganizado para que possa ser utilizado várias vezes
#A estrutura para criar uma funcao é a seguinte:
#def nomeFuncao (parametro1, parametro2, parametro3,..., parametroN):
#   com identacao aqui eh o corpo da funcao
# Vale lembrar que as funções podem ser de dois tipos: void (sem retorno) ou return (com retorno
#   return variavel

#Vale ressaltar que as variáveis que estão dentro da função, são serão vistas dentro da função (durante
# a execução da função) - variaveis globais (fora da função que são vistas em todos o código)

#Exemplo:

def imprimir (texto):
    print (texto)


def soma (x,y):
    return x + y



imprimir("Olá Mundo!")
print (soma(1,1))
import re
from math import sqrt

def calcular(expressao):

    numeros = []
    operadores = []


    #resolvendo parenteses
    def calcula_parenteseas(expressao):
        while '(' in expressao:
            inicio = expressao.rfind('(')
            fim = expressao.find(')', inicio)
            resultado_parenteses = calcular(expressao[inicio + 1: fim])
            expressao = expressao[:inicio] + str(resultado_parenteses) + expressao[fim + 1:]
        return expressao

    expressao = calcula_parenteseas(expressao)
    #Separando numeros de operadores
    numero_atual =''
    for i in expressao:
        if i.isdigit() or i == '.':
            numero_atual += i
        else:
            if numero_atual:
                numeros.append(float(numero_atual))
                numero_atual =''
            if i in ['+', '-', '/', '*', 'r', '^']:
                operadores.append(i)
    if numero_atual:
        numeros.append(float(numero_atual))


    #relizando raiz
    r = 0
    while r < len(operadores):
        if operadores[r] == "r":
            numeros[r] = sqrt(numeros[r])
            del operadores[r]
        r += 1

    #realizando Exponenciação
    e = 0
    while e < len(operadores):
        if operadores[e] == "^":
            if len(operadores) == len(numeros) and operadores[e+1] == '-':
                numeros[e] = (1/numeros[e]) ** numeros[e +1]
                del numeros[e+1]
                del operadores[e + 1]
                del operadores[e]

            else:
                numeros[e] = numeros[e] ** numeros[e +1]
                del numeros[e+1]
                del operadores[e]
        e += 1

    #Realizando operações de multiplicação e divisão
    z = 0
    while z < len(operadores):
        if operadores[z] == '*':
            numeros[z] = numeros[z] * numeros[z +1]
            del numeros[z+1]
            del operadores[z]
        elif operadores[z] == '/':
            if numeros[z+1] == 0:
               return print('ERRO! Não é possivel dividir por zero')
            else:
                numeros[z] = numeros[z] / numeros[z+1]
        z += 1

    #Realizando operações de adição e subtração
    resultado = numeros[0]
    for i in range(len(operadores)):
        if operadores[i] == '+':
            resultado += numeros[i + 1]
        elif operadores[i] == '-':
            resultado -= numeros[i + 1]
    return resultado

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# **************************************************************************
#                                                                         *
#   Camila Correa Vieira & Joao Cotta Badaró  							  *
#                                                                         *
# **************************************************************************

import sys

# Função recursiva que percorre a cadeia de símbolos
# até chegar a um estado final do autômato, se não chegar
# a nenhum estado final, retorna False.
def validaCadeiaSimbolos(cadeia, estado):
    global conj_estados_aceitacao, conj_transicoes
    # No final da cadeia de símbolos analisada, verifica
    # se o último estado encontrado está entre os estados
    # de aceitação. Se sim retorna True
    if cadeia == '':
        for estado_aceitacao in conj_estados_aceitacao:
            if estado_aceitacao == estado:
                return True
        return False
    simbolo = cadeia[0]
    #For para realizar a transição de estados
    #verificamos todos os caminhos possiveis
    for transicao in conj_transicoes:
        if (transicao[0] == estado) and (transicao[1] == simbolo):
            if validaCadeiaSimbolos(cadeia[1:], transicao[2]):
                return validaCadeiaSimbolos(cadeia[1:], transicao[2])
    return False


# Função que verifica uma cadeia, testando ela através
# de todos os estados iniciais do autômato
def testaCadeia(cadeia):
    global num_estados_iniciais
    # Testa a cadeia para todos os estados iniciais
    if validaCadeiaSimbolos(cadeia, num_estados_iniciais):
        return True
    # Se através de todos os estados iniciais
    # a cadeia não for reconhecida, retorna False
    return False


# Programa principal
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Número de argumentos inválido, tente novamente.")
        sys.exit(0)
    print("Trabalho LFA Camila Correa Vieira & Joao Cotta Badaró")

    # Recebe o nome do arquivo que será lido via parâmetro
    arquivo = sys.argv[1];
    # Tenta abrir o arquivo
    try:
        arquivo = open(arquivo, "r");
    except(IOError) as ex:
        print("Erro do tipo: ", ex)
        sys.exit(0)
    # Recebe o nome do arquivo que será escrito via parâmetro
    arquivo_saida = sys.argv[2];
    # Tenta criar o arquivo
    try:
        arquivo_saida = open(arquivo_saida, "w");
    except(IOError) as e6x:
        print("Erro do tipo: ", ex)
        sys.exit(0)

    # Número de estados do autômato
    num_estados = arquivo.readline()

    # Conjunto de símbolos terminais
    conj_simb_terminais = arquivo.readline()

    # Cria uma lista de símbolos terminais
    conj_simb_terminais = conj_simb_terminais.split()

    # Número de estados iniciais do autômato
    num_estados_iniciais = int(arquivo.readline())

    # Conjunto de estados de aceitação
    conj_estados_aceitacao = arquivo.readline()

    # Cria uma lista de estados de aceitação
    conj_estados_aceitacao = conj_estados_aceitacao.split()

    # convertendo valores da lista para inteiro
    conj_estados_aceitacao = list(map(int, conj_estados_aceitacao))
    # Número de transições
    num_transicoes = int(arquivo.readline())
    conj_transicoes = []

    # Laço para tratamento das transições
    for i in range(0, num_transicoes):
        transicao = arquivo.readline()
        # Cria uma lista onde:
        # - o primeiro valor é o estado de origem
        # - o segundo valor é o símbolo
        # - o terceiro valor é o estado de destino
        transicao = transicao.split()

        # convertendo os estados para inteiros,
        # provavelmente não é uma forma pythonica
        transicao[0] = int(transicao[0])
        transicao[2] = int(transicao[2])

        #If que verifica se o simbolo da transicao é valido
        #(esta presente na definicao do automato)
        if transicao[1] not in conj_simb_terminais:
            print("Simbolo de transicao inesistente")
            sys.exit(0)
        # Armazena a transição dentro da lista conj_transicoes
        conj_transicoes.append(transicao)

    # Número de cadeias de entrada
    num_cadeias_entradas = int(arquivo.readline())

    # Laço para tratamento de cadeias de entrada
    for i in range(0, num_cadeias_entradas):
        cadeia_atual = arquivo.readline().strip()

        if (testaCadeia(cadeia_atual)):
            print(cadeia_atual + " - Aceita")
            arquivo_saida.write(cadeia_atual +" Aceita\n")
        else:
            print(cadeia_atual + " - Rejeita")
            arquivo_saida.write(cadeia_atual + " Rejeita\n")

    # Libera o arquivo lido
    arquivo.close()
    arquivo_saida.close()

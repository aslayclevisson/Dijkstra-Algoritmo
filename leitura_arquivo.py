import random

def arquivo():
    arquivo = open("C:\\Users\\Aslay l Cynthia\\Documents\\ProjetoAlgoritmos\\ca-netscience.txt", "r") #obs isso está de acordo com o meu pc
    linhas = arquivo.readlines()
    linhas.append('\n')



    listaArestas = []
    #grafo = {}
    contador = 0
    index = ""

    for x in linhas:       
        for y in x:
            if y != " " and y != "\n":
                index += y
            
            if y == " ":
                listaArestas.append([(index)])
                index = ""

            if y == "\n":
                listaArestas[contador].append((index))                
                index = ""
                contador +=1



    for x in listaArestas:
        x.append(1)

    #print(listaArestas)
    return listaArestas

#arquivo()


import random

def arquivo():
    arquivo = open("C:\\Users\\marcs\\Documents\\UFPE\\Algoritmos\\Dijkstra\\ca-netscience.txt", "r") #obs isso está de acordo com o meu pc
    linhas = arquivo.readlines()
    linhas.append('\n')



    listaArestas = []
    #grafo = {}
    cont = 0
    idex = ""

    for x in linhas:
        
        for y in x:
            if y != " " and y != "\n":
                idex += y
            
            if y == " ":
                listaArestas.append([int(idex)])
                idex = ""
            if y == "\n":
                listaArestas[cont].append(int(idex))
                
                idex = ""
                cont +=1



    for x in listaArestas:
        x.append(random.randint(0,100))

    return listaArestas

print(arquivo())
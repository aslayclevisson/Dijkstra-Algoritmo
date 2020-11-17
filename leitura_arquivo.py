
def arquivo():
    arquivo = open("directory\\file.txt", "r")
    linhas = arquivo.readlines()
    linhas.append('\n')

    listaArestas = []
    contador = 0
    index = ""

    for v in linhas:       
        for elem in v:
            if elem != " " and elem != "\n":
                index += elem
            
            if elem == " ":
                listaArestas.append([(index)])
                index = ""

            if v == "\n":
                listaArestas[contador].append((index))                
                index = ""
                contador +=1

    for lista in listaArestas: 
        lista.append(1)

    #print(listaArestas)
    return listaArestas

#arquivo()


from cria_matriz import lista_matriz
import leitura_arquivo
import sys

class Dijkstra:
    def __init__(self, entrada):# a entrada conta com um dicionário com os todos_vertices e um grafo mostrado por lista de matriz
        self.instancia = lista_matriz(entrada) # puxa uma classe
        self.todos_vertices = 0 # onde vai ser armazenado todos os vertices da matriz por chaves de 0 a N
        self.todos_vertices_inversos = {} # esse dicionário vai usar todos os vertices como chave para os indices em que cada um se encontra
        self.lista_matriz_do_grafo = 0 # armazena uma lista de listas
        self.tamanho = 0 # pega a quantidade de vertices
        self.distancia = [] #Armazena as distâncias entre os vertices

    
 ###################################################################################################
    def comecar_e_terminar(self, inicio=None, ponto_final=None):
        try:
            print(f'Quero ir do ponto {inicio} até o ponto {ponto_final}.')
            print()

            if inicio != None and ponto_final != None:
                if inicio != ponto_final:
                    #A variável abaixo, evoca uma função que retorna os indices do ponto inicial e final trocados
                    #Basicamente, joga o Elemento Inicial pro indice 0 e o Elemento na posição 0, para o lugar onde antes tava o inicial
                    #O mesmo acontece com Elemento Final                    
                    self.todos_vertices = self.instancia.onde_comeca_e_onde_termina(inicio,ponto_final)

                    #monta um dicionário inverso, com os dados de todos os vertices inversos, ou seja, passa passa a ser valor e valor a chave
                    for i, j in self.todos_vertices.items():
                        self.todos_vertices_inversos[j] = i

                    self.tamanho = len(self.todos_vertices)
                    self.lista_matriz_do_grafo = self.instancia.pegar_arestas()
                    print('=#'*50)
                    print('Todos vertices -> ', self.todos_vertices)
                    print('Todos vertices inversos -> ', self.todos_vertices_inversos)
                    print('O grafo completo -> ',self.lista_matriz_do_grafo)
                    print('=#'*50)

                    self.dijkstra()
                else:
                    print(f'A distância entre {inicio} e {ponto_final} é igual a 0.')
        except:
            print('Um ou mais dos elementos não foram inseridos no grafo.')

###################################################################################################
    def encontrar_menor_distancia(self, distancia, visitados):
        try:
            minimo = sys.maxsize# adota um valor máximo
            menor_ind = 0
            distancia = distancia

            #Dá a distância mínima entre um vertice e o outro e retorna seu indice
            for vertice in range(self.tamanho):
                if distancia[vertice] < minimo and visitados[vertice] == False:
                    minimo = distancia[vertice]
                    menor_ind = vertice
         
            return menor_ind

        except:
            print('erro')

###################################################################################################   
    def dijkstra(self):
        self.distancia = [sys.maxsize] * self.tamanho# cria uma lista com valores máximos para serem substituido por mínimos de acordo com a quantidade de vertices
        visitados = [False] * self.tamanho# cria uma lista para substituir o False pelo True, quando algum vertice esteja sendo visitado
        self.distancia[0] = 0
        vertices = 0
        encontrou_ponto_final = False

        #
        for _ in range(self.tamanho):
            menor_indice = self.encontrar_menor_distancia(self.distancia, visitados)
            if visitados[menor_indice] == True:
                break

            visitados[menor_indice] = True  

            if self.todos_vertices[menor_indice] != self.todos_vertices[len(self.todos_vertices)-1]:
                print('Acabei de visitar --> ', self.todos_vertices[menor_indice])                
                #aqui vai ser verificado os adjacentes possíveis de visitar a partir de um vertice visitado
                for vertice in range(self.tamanho):                
                    #verifica se a coordenada se é maior que 0 e substitui os valores máximos em self.distância por novos valores reais de distância entre os vertices
                    if self.lista_matriz_do_grafo[menor_indice][vertice] > 0 and visitados[vertice] == False and self.distancia[vertice] > self.distancia[menor_indice] + self.lista_matriz_do_grafo[menor_indice][vertice]:
                        self.distancia[vertice] = self.distancia[menor_indice] + self.lista_matriz_do_grafo[menor_indice][vertice]# essa última parte é a soma dos valores das arestas

                        print('antecessor')
                        print('Estou em', self.todos_vertices[menor_indice])
                        print("Estou indo para --> ", self.todos_vertices[vertice])
                        print("Soma entre os valores anteriores até onde estou --> ", self.distancia[menor_indice])
                        print("Distância entre o vertice em que estou, até onde estou indo --> ", self.lista_matriz_do_grafo[menor_indice][vertice])
                        print("Soma da distância entre onde estou e onde estou indo --> ", self.distancia[vertice])
                        print()
                    vertices = vertice

            #Verifica se chegou no ponto final
            elif self.todos_vertices[menor_indice] == self.todos_vertices[len(self.todos_vertices)-1]:
                encontrou_ponto_final = True
                print(f'O visitado {self.todos_vertices[menor_indice]}, é o ponto final')
                print("Estou em --> ", self.todos_vertices[vertices])
                print(f'A menor soma do ponto {self.todos_vertices[0]} até onde estou -->  {self.distancia[menor_indice]}')
                print("Soma da distância entre onde estava e onde estou é --> ", self.distancia[vertices])
                print()
                print('='*30)
                break#Qualquer coisa, deixa ir
            print('='*30)

        #Verifica se algum caminho não pode ser visitado a partir do inicio
        if encontrou_ponto_final == False:
            print('Não há caminho para esse ponto.')

arquivo = leitura_arquivo.arquivo()
matriz_teste = [['346', '345', 1], ['346','349', 2], ['349', '348', 3], ['350', '348', 4], ['351', '348', 5], ['350', '349', 6], ['351', '349', 7],['350', '345', 8]]



dijkstra = Dijkstra(matriz_teste)
dijkstra.comecar_e_terminar('345','349')






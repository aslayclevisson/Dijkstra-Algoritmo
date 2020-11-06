import numpy as np
import leitura_arquivo

class lista_matriz:
    def __init__(self, entrada):
        self.entrada = entrada
        self.vertices_inversos = {}
        self.vertices = {}
        self.rotas = {}
        self.cont = 0
        self.arestas = self.retorna_matriz()
        self.caminhos = []

###################################################################################################
    def onde_comeca_e_onde_termina(self, inicio=None, ponto_final=None):
        if inicio != None and ponto_final != None:# condicao 4
            for chave, valor in self.vertices_inversos.items():
                self.vertices[valor] = chave

            self.vertices[0], self.vertices[self.vertices_inversos[inicio]] = self.vertices[self.vertices_inversos[inicio]], self.vertices[0]
            self.vertices_inversos[self.vertices[self.vertices_inversos[inicio]]], self.vertices_inversos[inicio] = self.vertices_inversos[inicio], self.vertices_inversos[self.vertices[self.vertices_inversos[inicio]]]
            
            self.vertices[len(self.vertices_inversos)-1], self.vertices[self.vertices_inversos[ponto_final]] = self.vertices[self.vertices_inversos[ponto_final]], self.vertices[len(self.vertices_inversos)-1]
            self.vertices_inversos[self.vertices[self.vertices_inversos[ponto_final]]], self.vertices_inversos[ponto_final] = self.vertices_inversos[ponto_final], self.vertices_inversos[self.vertices[self.vertices_inversos[ponto_final]]]
            
            return self.vertices

###################################################################################################
    def retorna_matriz(self):
        lista_boa = []
        
        for lista in self.entrada:
            for indice in range(len(lista)-1):
                if lista[indice] not in self.vertices_inversos:
                    self.vertices_inversos[lista[indice]] = self.cont
                    self.cont+=1

        for chave, valor in self.vertices_inversos.items():
            self.rotas[valor] = chave
        

        for indice in range(len(self.rotas)):
            lista_boa.append([])
            for _ in range(len(self.vertices_inversos)):
                lista_boa[indice].append(0)


        if len(lista_boa) == len(lista_boa[0]):
            return lista_boa

###################################################################################################
    def recebe_valor(self, bairro1, bairro2, distancia):
        self.arestas[self.vertices_inversos[bairro1]][self.vertices_inversos[bairro2]] = distancia
        self.arestas[self.vertices_inversos[bairro2]][self.vertices_inversos[bairro1]] = distancia
  
################################################################################################### 
    def pegar_arestas(self):
        for lista in self.entrada:
            self.recebe_valor(lista[0], lista[1], lista[2])

        return self.arestas
    


#a = leitura_arquivo.arquivo()
#h = [['346', '345', 1],['346', '349', 2], ['349', '348', 3], ['350', '348', 4], ['351', '348', 5], ['350', '349', 6], ['351', '349', 7],['350', '345', 8]]#[['346', '345', 1], ['349', '348', 2], ['350', '348', 3], ['351', '348', 6], ['350', '349', 2], ['351', '349', 20],['350', '345', 20]]

#matriz = lista_matriz(h)
#matriz.onde_comeca_e_onde_termina('345','349')
#matriz.pegar_arestas()
#matriz.pegar_rotas()
#matriz.pegar_vertices()
#matriz.dar_valor()


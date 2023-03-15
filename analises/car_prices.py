import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#plt.style.use('_mpl-gallery')

#As análises nesse código não ocorrerão em formato de subplot, são apenas testes de visual

#Realizando uma visualização analítica entre o comprimento e os eixos dos carros na lista
dataset = pd.read_csv('databases/car_price.csv')
plt.scatter(dataset['wheelbase'], dataset['carlength'], s=25)
plt.xlabel('Distância entre eixos')
plt.ylabel('Comprimento')
plt.grid()
plt.show()

#Análise da % da quantidade de tipos de combustíveis
plt.pie(dataset['fueltype'].value_counts(), #Dados que serão utilizados
        radius=1, #Setando o raio do gráfico de pizza
        wedgeprops={"linewidth": 1, "edgecolor": "white"}, #Propriedade das linhas divisórias de cada pedaço
        labels=("Gasolina", "Diesel"), #Legenda (segue o padrão de x, y)
        shadow=True, #Criação de sombra no gráfico
        explode=(0, 0.5), #Deslocamento do pedaço da pizza
        autopct='%.2f%%') #Porcentagem automatica. Lê os dados e transforma em %. Ler função format em caso de dúvidas.
plt.title('Tipos de combustíveis por carro')
plt.show()

#Criando uma função de tradução
def tradutor(a):
        if a == 'two':
            return 'Dois'
        elif a == 'four':
            return 'Quatro'
        elif a == 'six':
            return 'Seis'
        elif a == 'five':
            return 'Cinco'
        elif a == 'three':
            return 'Três'
        elif a == 'twelve':
            return 'Doze'
        else:
            return 'Oito'

#Aplicando a função de tradução diretamente no dataset
dataset['cylindernumber'] = dataset['cylindernumber'].apply(tradutor)

#Aplicando o código de barras
plt.bar(dataset['cylindernumber'].unique(), 
        dataset['cylindernumber'].value_counts(), 
        width=1, 
        edgecolor='black', 
        linewidth=1)
plt.show()
#plt.bar()
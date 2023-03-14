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



plt.pie(dataset['fueltype'].value_counts(), radius=2)
plt
plt.show()


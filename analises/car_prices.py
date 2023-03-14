import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('_mpl-gallery')

#Realizando uma visualização analítica entre o comprimento e os eixos dos carros na lista
dataset = pd.read_csv('databases/car_price.csv')
plt.scatter(dataset['wheelbase'], dataset['carlength'], s=25)
plt.xlabel('Distância entre eixos')
plt.ylabel('Comprimento')
plt.show()

#...................parcial WILLLIAM VELEZ MESA................#

import matplotlib.pyplot as plt
import pandas as pd

snack1 = input("Ingresa tu snack favorito: ")
precio1 = int(input("Ingresa el precio de este snack: "))
snack2 = input("Ingresa tu snack favorito: ")
precio2 = int(input("Ingresa el precio de este snack: "))
snack3 = input("Ingresa tu snack favorito: ")
precio3 = int(input("Ingresa el precio de este snack: "))
snack4 = input("Ingresa tu snack favorito: ")
precio4 = int(input("Ingresa el precio de este snack: "))
snack5 = input("Ingresa tu snack favorito: ")
precio5 = int(input("Ingresa el precio de este snack: "))

lista_snacks = [snack1, snack2, snack3, snack4, snack5]
lista_precios = [precio1, precio2, precio3, precio4, precio5]

plt.bar(lista_snacks, lista_precios)
plt.xlabel("snacks")
plt.ylabel("precio")
plt.title("grafica de barras")
plt.savefig("barras.png")
plt.show()

cuidad1 = input("Ingresa tu cuidad favorita: ")
poblacion1 = int(input("Ingresa la poblacion de esta cuidad: "))
cuidad2 = input("Ingresa tu cuidad favorita: ")
poblacion2 = int(input("Ingresa la poblacion de esta cuidad: "))
cuidad3 = input("Ingresa tu cuidad favorita: ")
poblacion3 = int(input("Ingresa la poblacion de esta cuidad: "))
cuidad4 = input("Ingresa tu cuidad favorita: ")
poblacion4 = int(input("Ingresa la poblacion de esta cuidad: "))
cuidad5 = input("Ingresa tu cuidad favorita: ")
poblacion5 = int(input("Ingresa la poblacion de esta cuidad: "))

lista_cuidades = [cuidad1, cuidad2, cuidad3, cuidad4, cuidad5]
lista_poblaciones = [poblacion1, poblacion2, poblacion3, poblacion4, poblacion5]
explode=[0, 0, 0, 0, 0]

maximo = max(lista_poblaciones)
ubicacion = lista_poblaciones.index(maximo)
explode[ubicacion] = 0.1

plt.pie(lista_poblaciones, explode, labels=lista_cuidades)
plt.title("grafica de torta")
plt.savefig("torta.png")
plt.show()

print("Definicion ecg: El electrocardiograma es la representación visual de la actividad eléctrica del corazón en función del tiempo, que se obtiene, desde la superficie corporal, en el pecho, con un electrocardiógrafo en forma de cinta continua.")
print("Definicion ppg; La fotopletismografía o fotopletismograma es una técnica de pletismografía en la cual se utiliza un haz de luz para determinar el volumen de un órgano.")

df = pd.read_csv("ecg.csv", sep=";")
valor_ecg = df["valor"]

plt.plot(valor_ecg)
plt.title("Grafica ECG")
plt.xlabel("tiempo")
plt.ylabel("mV")
plt.savefig("ecg.png")
plt.show()

df2 = pd.read_csv("ppg.csv", sep=";")
valor_ppg = df2["valor"]

plt.plot(valor_ppg)
plt.title("Grafica PPG")
plt.xlabel("tiempo")
plt.ylabel("volumen")
plt.savefig("ppg.png")
plt.show()
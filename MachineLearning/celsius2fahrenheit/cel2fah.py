import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Inicializamos la capa de salida con keras
# units=1 (1 neurona de salida), input_shape=[1] (1 neurona de entrada)
capa = tf.keras.layers.Dense(units=1, input_shape=[1])

# definimos un modelo Sequential
modelo = tf.keras.Sequential([capa])

# Compilamos el modelo, para que pueda ser entrenado
modelo.compile(
    # Con Adam le va ir diciendo como ajustar sus pesos y sesgos de manera eficiente,
    # para que aprenda y no desaprenda. 0.1 es la taza de aprendizaje y se utiliza
    # para saber que tango ajustar los pesos y sesgos; un número muy pequeño hará que
    # avance muy lento, con un número grande puede hacer que se pase.
    optimizer=tf.keras.optimizers.Adam(0.1),
    # Usaremos la función de pérdida del error cuadrático medio. Considera que una poca
    # cantidad de errores grandes, es peor que una gran cantidad de errores pequeños.
    loss='mean_squared_error'
)

# A entrenarlo
print("Iniciando entrenamiento...")
# epochs=1000 dara 1000 vueltas a los 7 datos de entrenamiento que tenemos
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Termina entrenamiento")

# Graficamos la función de pérdida donde nos dice qué tan mal están los resultados
# de la red, en cada vuelta que dio
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import warnings

# Desactivar advertencias de deprecación
warnings.filterwarnings("ignore", category=DeprecationWarning)

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Inicializamos la capa de salida con Keras
capa = tf.keras.layers.Dense(units=1, input_shape=[1])

# Definimos un modelo Sequential
modelo = tf.keras.Sequential([capa])

# Compilamos el modelo
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss=tf.keras.losses.MeanSquaredError()
)

# A entrenarlo
print("Iniciando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Termina entrenamiento")

# Graficamos la función de pérdida
# Nos damos cuenta a a partir de la vuelta 500 dejo de aprender, entonces podemos
# modificar nuestro epochs a 500
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])
plt.show()

# Una predicción con este entrenamiento
print("Hagamos una predicción.")
resultado = modelo.predict([100.0])
print("100 °C me dice que son " + str(resultado) + " °F")

# Veamos los valores del peso (primer valor mostrado) y el sesgo (segundo valor mostrado)
# calculado con el entrenamiento
print("Variables internas del modelo")
print(capa.get_weights())

modelo.save("cel2fah_entrenado_v1.h5")

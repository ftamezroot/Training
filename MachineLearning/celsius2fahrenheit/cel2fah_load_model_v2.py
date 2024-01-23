import tensorflow as tf
import numpy as np

# Cargar el modelo
modelo_cargado = tf.keras.models.load_model("cel2fah_entrenado_v2.h5")

# Ejemplo de predicción
# nueva_data = np.array([-32.5, 57], dtype=float)
# predicciones = modelo_cargado.predict(nueva_data)
# print("Predicciones:", predicciones)
while True:
    input_celsius = input('Grados celsius?:')
    nueva_data = np.array([input_celsius], dtype=float)
    prediccion = modelo_cargado.predict([nueva_data])
    print(input_celsius, "°C = ", prediccion, "°F")

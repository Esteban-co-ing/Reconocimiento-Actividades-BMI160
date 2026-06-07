# Reconocimiento-Actividades-BMI160
Sistema de reconocimiento de actividades humanas utilizando un sensor IMU BMI160 y Machine Learning ejecutado en una Raspberry Pi. 

El sistema captura datos de acelerómetro y giroscopio, procesa las señales y clasifica diferentes movimientos en tiempo real.

# Demostración

<div align="center">
<p align="center">
  <video src="https://github.com/user-attachments/assets/cdbe5223-6774-4d73-8c6f-962647e2567e" controls width="600"></video>
</p>
</div>

# Descripción

Este proyecto implementa un sistema capaz de reconocer actividades humanas mediante señales inerciales obtenidas desde un sensor BMI160.

El sensor se comunica con una Raspberry Pi mediante protocolo I2C y los datos son procesados usando un modelo de Machine Learning previamente entrenado.

# Actividades reconocidas

El sistema identifica:

- Caminar
- Sentarse
- Movimiento de torso
- Saltar

# Hardware utilizado

- Arduino
- Raspberry Pi
- Sensor BMI160 (acelerómetro + giroscopio)
- Comunicación I2C

# Adquisición de datos y creación de la base de datos

A través del código **"CodigoTomadeDatos.ino"**, junto con un Arduino UNO y un interruptor, se realizó la adquisición de datos de forma alámbrica.

Se registraron datos de 10 personas realizando las 4 actividades descritas anteriormente.

Los datos fueron almacenados en formato **.CSV**, imprimiendo la información obtenida en el monitor serial.

Posteriormente, se utilizó el programa **CoolTerm** para capturar la salida serial y convertirla en archivos de texto (.TXT), con valores separados por comas.

La base de datos obtenida se encuentra comprimida en el archivo **"BasedeDatosMovimiento.rar"**.

# Entrenamiento de los modelos

El sensor proporciona seis variables de entrada:

- Acelerómetro en los ejes X, Y y Z  
- Giroscopio en los ejes X, Y y Z  

A partir del cuaderno de Google Colab **"P6acelerometro.ipynb"**, se procesaron los datos obtenidos de los 10 participantes y se entrenaron dos modelos de clasificación utilizando la librería Scikit-learn.

## Modelos evaluados

- Árbol de decisión  
- Random Forest  

## Modelos entrenados

Los modelos generados se almacenan en archivos serializados (.pkl):

- `finalized_model_dt_pickle.pkl`  
- `finalized_model_rf_pickle.pkl`  

## Acceso al modelo Random Forest

El modelo Random Forest no se encuentra incluido directamente en este repositorio debido a su tamaño.

Puede descargarse desde Google Drive en el siguiente enlace:

🔗 [Descargar modelo Random Forest](https://drive.google.com/file/d/1R9d0_01hZPT8YW2uegTcv7B9Y_5f_azv/view?usp=sharing)

Alternativamente, el modelo puede ser reproducido ejecutando el cuaderno de entrenamiento `P6acelerometro.ipynb`.

## Uso del modelo

Los modelos entrenados se utilizan posteriormente para realizar predicciones en tiempo real a partir de los datos del sensor.

# Funcionamiento del sistema

El sistema se ejecuta conectando el sensor a una Raspberry Pi, donde se ejecuta el script `movimiento.py`.

En este código, en primer lugar se cargan los datos utilizados durante el entrenamiento con el fin de obtener los mismos parámetros de normalización empleados en el modelo mediante `MinMaxScaler`.

Posteriormente, se realiza la lectura de los datos del sensor en tiempo real, se aplica la misma normalización utilizada durante el entrenamiento y se ejecuta la predicción utilizando el modelo Random Forest.

Finalmente, la actividad detectada se muestra en la consola.

# Alcances y mejoras futuras

En general, el sistema funcionó adecuadamente para la detección de las actividades: sentarse, movimiento de torso y saltar. Sin embargo, la actividad de caminar no fue reconocida con buena precisión.

Se recomienda incrementar la cantidad de datos de entrenamiento, especialmente para mejorar la representación de aquellas clases con menor desempeño.

Por otra parte, habría sido conveniente incluir una clase adicional correspondiente a un estado neutro (por ejemplo, de pie en reposo), lo cual permitiría mejorar la capacidad de clasificación del modelo en situaciones reales.

Asimismo, un sistema inalámbrico sería una mejora importante, ya que actualmente la comunicación I2C se realiza mediante un cable de aproximadamente 7 metros.

En el código de entrenamiento, las variables del sensor fueron nombradas como A, B, C, x, y, z, lo cual puede generar confusión. Una nomenclatura más descriptiva como AccX, AccY, AccZ, GyroX, GyroY y GyroZ sería más apropiada.

Finalmente, en la implementación en Raspberry Pi, resulta poco práctico volver a cargar el dataset para obtener los parámetros de normalización. Sería más eficiente exportar directamente el `MinMaxScaler` entrenado o sus parámetros, evitando dependencias del conjunto de datos durante la inferencia.
  

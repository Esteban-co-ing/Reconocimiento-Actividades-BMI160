# Reconocimiento-Actividades-BMI160
Sistema de reconocimiento de actividades humanas utilizando un sensor IMU BMI160 y Machine Learning ejecutado en una Raspberry Pi. 

El sistema captura datos de acelerómetro y giroscopio, procesa las señales y clasifica diferentes movimientos en tiempo real.

# Demostración

<div align="center">
<p align="center">
  <video src="https://github.com/user-attachments/assets/92d76824-e11b-4493-bbe8-c0d228bad55f" controls width="600"></video>
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

La base de datos obtenida se encuentra comprimida en el archivo **BasedeDatosMovimiento.rar**.

# Entrenamiento de los modelos

# Funcionamiento del sistema

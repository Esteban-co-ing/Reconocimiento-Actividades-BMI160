#include <DFRobot_BMI160.h> //Libreria del sensor que controla la comunicación I2C

DFRobot_BMI160 bmi160; //Objeto para las funciones de la libreria

int interruptor = LOW; 
int interruptorant = LOW;
int actividad = 0; //Indica el tipo de actividad que esta registrando el sensor (Actividad tipo 1,2,3.....)

const int8_t i2c_addr = 0x68;
void setup(){
  pinMode(11,INPUT); //Se lee el interruptor que permite detener la lectura de datos de una actividad para luego, al volverlo a mover, pasar a registrar la siguiente actividad
  pinMode(13, OUTPUT);  
  digitalWrite(13, HIGH); //Una salida de 5V para facilidad de configurar el interruptor
  Serial.begin(115200); //Se abre la comunicación serial
  delay(100);
  
  //Se reinicia el sensor
  if (bmi160.softReset() != BMI160_OK){
    Serial.println("reset false");
    while(1);
  }
  
  //Se inicia la comunicacion con el sensor a través de la dirección I2C. Si falla, no continua el programa
  if (bmi160.I2cInit(i2c_addr) != BMI160_OK){
    Serial.println("init false");
    while(1);
  }
}

void loop(){
  interruptor = digitalRead(11); //Se lee el estado del interruptor

  if(interruptorant==LOW && interruptor==HIGH){ //Si se detecta un flanco de subida del interruptor es porque se cambio de actividad
    actividad = actividad + 1; //Se pasa al siguiente tipo de actividad
  }

  if(interruptor == HIGH){ //El interruptor esta en estado HIGH y se registran datos de forma contante para un unico tipo de actividad
    int i = 0;
    int rslt;
    int16_t accelGyro[6]={0}; //Arreglo donde se guardaran los datos de giroscopio y acelerometro del sensor
    rslt = bmi160.getAccelGyroData(accelGyro); //Se guardan los datos del sensor en el arreglo accelGyro y se define rslt como el estado de la lectura
    if(rslt == 0){//Si no hubo error en la lectura del sensor rslt=0
      for(i=0;i<6;i++){//Con este condicional se imprime la lectura del sensor por el puerto serial
        if (i==5){
          Serial.print(accelGyro[i]);
          Serial.print(",");
          Serial.print(actividad); //Al imprimir el ultimo valor del arreglo accelGyro, se imprime el valor del tipo de actividad
        }else{
          Serial.print(accelGyro[i]);
          Serial.print(",");
        }
      }
      Serial.println();//Se cambia de linea por cada lectura del sensor
    }else{
      Serial.println("err");
    }
  }

  interruptorant = interruptor; //Se guarda el valor anterior de interruptor para detectar los flancos de subida
  delay(2); //retardo minimo para guardar datos lo mas rapido posible, sin embargo, el retardo real es lo que tarde el sensor en responder y el puerto serial
}











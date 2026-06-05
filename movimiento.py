#En este punto se repite el proceso de leer los datos .CSV hecho en el libro Colab, todo con el fin de obtener el objeto scaler con los mismos parametros con los que se entreno el modelo 
import pandas as pd
import os
os.environ['PYTHONHASHSEED'] = str(1)
import pickle
import joblib
import sklearn.preprocessing as skp
import sklearn.tree as skt
def borrar_consola():
    os.system('clear')

DIR = '/home/joespi/datos/' #Ubicacion de los .CSV en la raspberry
df = pd.DataFrame()
for x in range(1,11):
    df_temp = pd.read_csv(os.path.join(DIR, str(x)+'.csv'))
    df_temp.columns = ['A','B','C','x','y','z','class']
    df_temp['person'] = x
    df = pd.concat([df, df_temp], axis=0)


index_label = dict()
index_label[0] = "None"
index_label[1] = "Caminar"
index_label[2] = "sentarse"
index_label[3] = "mover el torso"
index_label[4] = "saltar"

df = df[~df["class"].isin([0])]
X_train = df[df['person'] <= 7]
X_test = df[df['person'] > 7]
y_train = X_train.pop('class')
y_test = X_test.pop('class')


X_train.drop('person', axis=1, inplace=True)
X_test.drop('person', axis=1, inplace=True)
print(X_test.shape)
scaler = skp.MinMaxScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns) #Aquí se obtiene el objeto scaler que adapta los datos leídos por el sensor y los normaliza con los mismos parámetros que se usaron para ajustar los datos en el entrenamiento
X_test = pd.DataFrame(scaler.transform(X_test), columns=X_train.columns)



with open('/home/joespi/finalized_model_rf_pickle.pkl', 'rb') as file:
    modelo = pickle.load(file) #Se abre el archivo .pkl que contiene el modelo entrenado

print(modelo)
from time import sleep
from BMI160_i2c import Driver #Se crea un objeto con la librería que controla al sensor BMI160 por comunicación I2C
sensor = Driver(0x69) #Dirección I2C del sensor

while True:
    data = sensor.getMotion6() #Se obtienen los 6 valores del sensor
    X_leido = ([100,100,100,100,100,100],[data[0],data[1],data[2],data[3],data[4],data[5]]) #Como scaler.transform espera un arreglo 2D, se crean dos filas, la primera con valores basura de 100 y la segunda con los valores reales del sensor
    X_leido = pd.DataFrame(scaler.transform(X_leido), columns=X_train.columns) #Se escalan los datos del sensor con el mismo criterio que se uso en el entrenamiento
    predicciones = modelo.predict(X_leido) #Se aplica el modelo a los datos obtenidos en tiempo real del sensor
    if predicciones[1] == 1: #Aquí se convierten los numeros de salida del modelo a las actividades que corresponden
        print("caminar")
    elif predicciones[1]==2:
        print("sentado")
    elif predicciones[1]==3:
        print("girar")
    elif predicciones[1]==4:
        print("saltar")
    sleep(2) #Se espera dos segundos antes de clasificar otra vez
    borrar_consola() #Se limpia la consola donde se muestran los resultados para que no se amontonen uno sobre otro

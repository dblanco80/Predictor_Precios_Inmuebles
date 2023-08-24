from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

modelo = pickle.load(open('modelo_entrenado.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predecir():
    print('ingreso a predict')
    lat = float(request.form.get('lat'))
    lon = float(request.form.get('lon'))
    amb = int(request.form.get('amb'))
    banios = int(request.form.get('banios'))
    sup_tot = float(request.form.get('sup_tot'))
    sup_cub = float(request.form.get('sup_cub'))
    
    data = {
    'lat': lat,
    'lon': lon,
    'ambientes': amb,
    'banios': banios,
    'sup_total': sup_tot,
    'sup_cub': sup_cub
    }

    df_prediccion = pd.DataFrame(data,index=[0])
    
    result = modelo.predict(df_prediccion)
    
    #result = modelo.predict(np.array([lat,lon,amb,banios,sup_tot,sup_cub]).reshape(1,6))
    
    result = np.round(np.exp(result),2)
    
    return render_template('index.html',result=result)

if __name__ == '__main__':
    app.run(0.0.0.0)
    

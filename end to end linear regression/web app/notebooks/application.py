from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)

app = application



#import ridge regressor and standart scaler piclke
import joblib
ridge_model = joblib.load('/mnt/c/Users/sm1523/Desktop/NLP-main/end to end linear regression/web app/models/house_price_model.pkl')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        MedInc = float(request.form.get('MedInc'))
        HouseAge = float(request.form.get('HouseAge'))
        AveRooms = float(request.form.get('AveRooms'))
        AveBedrms = float(request.form.get('AveBedrms'))
        Population = float(request.form.get('Population'))
        AveOccup = float(request.form.get('AveOccup'))
        Latitude = float(request.form.get('Latitude'))
        Longitude = float(request.form.get('Longitude')) 
        new_data = [MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude]
        result = ridge_model.predict([new_data])
        return render_template('home.html',results=result   )  
    else:
        return render_template('home.html')
    
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

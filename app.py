from flask import Flask,request,render_template,url_for
from flask_cors import cross_origin
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)
model= pickle.load(open("xgboost.pickle","rb"))
@app.route('/')
def home():
    return render_template("home.html")

@app.route("/predict",methods= ["GET","POST"])
def predict():
    if request.method =="POST":
        #1. 
        workingday=request.form["workingday"]
        if (workingday=="yes"):
            workingday=1
        else:
            workingday=0
        
        #2.
        temperature=float(request.form["temperature"])
        
        #3.
        humidity=int(request.form["humidity"])
        
        #4.
        windspeed=float(request.form["windspeed"])
        
        #5.
        weekday=request.form["weekday"]
        if (weekday=="sun"):
            weekday=0
        elif (weekday=="mon"):
            weekday=1
        elif (weekday=="tue"):
            weekday=2
        elif (weekday=="wed"):
            weekday=3
        elif (weekday=="thu"):
            weekday=4
        elif  (weekday=="fri"):
            weekday=5
        else:
            weekday=6
        
        #6.
        hour=int(request.form["hour"])
        
        #7.
        month=request.form["month"]
        if (month=="jan"):
            month=1
        elif (month=="feb"):
            month=2
        elif (month=="mar"):
            month=3
        elif (month=="apr"):
            month=4
        elif (month=="may"):
            month=5
        elif (month=="jun"):
            month=6
        elif (month=="jul"):
            month=7
        elif (month=="aug"):
            month=8
        elif (month=="sep"):
            month=9
        elif (month=="oct"):
            month=10
        elif (month=="nov"):
            month=11
        else:
            month=12
        
        #8.
        season=request.form["season"]
        if (season=="spring"):
            spring=1
            summer=0
            winter=0
        elif (season=="summer"):
            spring=0
            summer=1
            winter=0
        elif (season=="autumn"):
            spring=0
            summer=0
            winter=0
        else:
            spring=0
            summer=0
            winter=1
        weather=request.form["weather"]
        if (weather=="heavy"):
            heavy=1
            light=0
            mist=0
        elif (weather=="light"):
            heavy=0
            light=1
            mist=0
        elif (weather=="mist"):
            heavy=0
            light=0
            mist=1
        
        else:
            heavy=0
            light=0
            mist=0
        pred=pd.read_csv('pred.csv')
        pred.iloc[:1,:]=[workingday, temperature, humidity, windspeed, weekday, hour, month,
                          spring,summer ,winter, heavy,light,mist]
        bookings=model.predict(pred)[0]
        return render_template("home.html",prediction_text="Your number of bookings are **{}**".format(int(bookings)))
    
    return render_template("home.html")
    
if __name__ == '__main__':
    app.run()
    print(predict())
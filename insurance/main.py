import numpy as np
import joblib
model=joblib.load('linear_model.lb')
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('dashboard.html')  
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')
@app.route('/policies')
def policies():
    return render_template('policies.html')
@app.route('/settings')
def settings():
    return render_template('settings.html')
@app.route('/insights')
def insights():
    return render_template('ai-insights.html')
@app.route('/analytics')
def analytics():
    return render_template('analytics.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        age=int(request.form['age'])
        gender=request.form['gender']
        bmi=float(request.form['bmi'])
        children=int(request.form['children'])
        smoker=request.form['smoker']
        region=request.form['region']
        print(">>>>>>",gender,smoker,region)
        gender_dict={
    'female':1, 'male':2
    }
        gender=gender_dict[gender]
        smoker_dict={
    'yes':1, 'no':0
}
        smoker=smoker_dict[smoker]
        region_dict={
    'southwest':1, 'southeast':2, 'northwest':3, 'northeast':4
}
        region=region_dict[region]
        print("lables:-",age,gender,bmi,children,smoker,region)
        lables=[[age,gender,bmi,children,smoker,region]]
        pred=model.predict(lables)
        print(type(pred ))
        pred=np.ravel(pred)
        print("output:-",pred)
        return render_template('predict.html',prediction=pred)
    return render_template('predict.html')
if __name__=='__main__':
    app.run(debug=True) 
from flask import Flask,render_template,request
from Diabetes_Prediction_knn import prediction
app=Flask(__name__)

pr=0
@app.route("/",methods=["GET","POST"])
def home_page():
    if request.method=="GET":
        print("Get Method is There")
        print(request.args.get("nameInp"))
    return render_template("index.html")

@app.route("/result",methods=["GET","POST"])
def nextPage():
    global pr
    if request.method=="POST":
        preg=float(request.form['Pregnancies'])
        glucose=float(request.form['Glucose'])
        bloodPressure=float(request.form['BloodPressure'])
        skinThinkness=float(request.form['SkinThickness'])
        insulin=float(request.form['Insulin'])
        bmi=float(request.form['BMI'])
        dpf=float(request.form['DiabetesPedigreeFunction'])
        age=float(request.form['Age'])
        pr=prediction([preg,glucose,bloodPressure,skinThinkness,insulin,bmi,dpf,age])
        if pr==1:
            # print("Yes you can be a diabetic patient...")
            return render_template("patient.html")
        else:
            return render_template("notPatient.html")

    return render_template("diacare.html")

if __name__=="__main__":
    app.run(debug=True)
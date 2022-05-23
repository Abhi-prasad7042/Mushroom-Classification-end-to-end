from flask import Flask,render_template, request
import numpy as np
import joblib
import os

webapp_root = "webapp"
template_dir = os.path.join(webapp_root,"templates")

model = joblib.load("models/model.joblib")

app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def index():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    final_feat = list(request.form.values())
    final_Feat = [int(i) for i in final_feat]
    final_feat = np.array(final_feat).reshape(1,14)

    output = model.predict(final_feat)[0]

    return render_template("predict.html",output=output)

if __name__ =="__main__":
    app.run(debug=True)
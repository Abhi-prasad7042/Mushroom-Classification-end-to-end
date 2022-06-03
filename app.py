from flask import Flask,render_template, request
import numpy as np
import joblib
import os
import logging

logging.basicConfig(filename="logs/deployment_logs.logs",filemode="w",format='%(asctime)s %(levelname)s %(message)s', level = logging.INFO)

webapp_root = "webapp"
template_dir = os.path.join(webapp_root,"templates")
logging.info("template_dir linked succssfully")

model = joblib.load("models/model.joblib")
logging.info("model load successfully")

app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def index():
    try:
        return render_template("home.html")
    except Exception as e:
        logging.error(e)

@app.route("/about")
def about():
    try:
        return render_template("about.html")
    except Exception as e:
        logging.error(e)

@app.route('/predict',methods=['POST'])
def predict():
    try:
        final_feat = list(request.form.values())
        final_Feat = [int(i) for i in final_feat]
        final_feat = np.array(final_feat).reshape(1,14)

        output = model.predict(final_feat)[0]
        return render_template("predict.html",output=output)

    except Exception as e:
        logging.error(e)

if __name__ =="__main__":
    logging.info("Application running succussfully")
    app.run(debug=True)
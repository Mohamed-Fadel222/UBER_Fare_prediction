import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_frozen  import Freezer
import pickle


# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("XGboost.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")
    

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html", prediction_text = "The Uber Fare is {}".format(prediction))

if __name__ == "__main__":
    freezer = Freezer(flask_app)
    freezer.freeze()
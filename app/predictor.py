import joblib
import pandas as pd

MODEL_PATH = "model/fraud_pipeline.pkl"

model = joblib.load(MODEL_PATH)

def predict(data):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return prediction, probability
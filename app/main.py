from fastapi import FastAPI
from app.schema import Transaction
from app.predictor import predict

app = FastAPI(title="Credit Card Fraud Detection API")

@app.get("/")
def home():
    return {"message": "Fraud Detection API running"}

@app.post("/predict")
def predict_fraud(transaction: Transaction):

    data = transaction.dict()

    pred, prob = predict(data)

    return {
        "fraud_prediction": int(pred), # 0 -> not fraud, 1 -> fraud
        "fraud_probability": float(prob)
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}
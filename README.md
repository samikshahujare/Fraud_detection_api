# Credit Card Fraud Detection API

![Python](https://img.shields.io/badge/python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)


# 1. Problem Description

Credit card fraud is a major issue for financial institutions. Fraudulent transactions represent only a very small portion of total transactions, but they can result in significant financial losses.

Detecting fraud manually is difficult because:

* Fraudulent transactions are rare
* Fraud patterns evolve over time
* Human inspection is slow and expensive

The objective of this project is to automatically detect fraudulent credit card transactions using machine learning.

The model classifies each transaction into:

* Legitimate Transaction
* Fraudulent Transaction

This system can help financial institutions:

* Detect suspicious activity in real time
* Reduce financial losses
* Improve fraud monitoring systems


# 2. Dataset

Source: Kaggle
Link: [https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

### Dataset Characteristics

* 284,807 transactions
* Highly imbalanced dataset
* Only 492 fraud cases

### Feature Description

Time – seconds elapsed between transactions  
V1 – V28 – anonymized features obtained through PCA transformation  
Amount – transaction amount  
Class – target variable (0 = legitimate, 1 = fraud)

Due to confidentiality reasons, the original features are not available and have been transformed using Principal Component Analysis (PCA).


# 3. Exploratory Data Analysis (EDA)

The following analysis was performed during exploration:

* Verified class imbalance
* Analyzed transaction amount distribution
* Inspected fraud vs legitimate transaction patterns
* Checked feature distributions
* Identified correlations between PCA features

### Observations

* Fraudulent transactions represent less than 0.2% of the dataset
* Class imbalance is extreme
* Standard accuracy is not an appropriate metric
* Recall and ROC-AUC are more meaningful metrics

Handling class imbalance is therefore critical for building an effective model.


# 4. Model Training

### Handling Class Imbalance

To address the imbalance problem, the following techniques were explored:

* SMOTE (Synthetic Minority Oversampling)
* Balanced class weights
* Stratified train-test split

### Models Evaluated

* Logistic Regression
* Random Forest
* XGBoost

### Final Model Selection

The final model was selected based on performance on:

* ROC-AUC
* Recall
* F1 Score

### Model Performance

| Metric   | Score |
| -------- | ----- |
| ROC-AUC  | ~0.97 |
| Recall   | ~0.84 |
| F1 Score | ~0.79 |

High recall is important because missing fraudulent transactions can lead to financial loss.


# 5. Model Export

After training, the model pipeline was exported using Joblib.

The exported pipeline includes:

* preprocessing steps
* sampling strategy
* trained model

The model artifact is stored at:

model/fraud_pipeline.pkl

This pipeline can be directly loaded for inference.


# 6. Inference Service

The trained model is exposed through a REST API built using FastAPI.

### API Input

Transaction features in JSON format:

V1 – V28
Amount

### API Output

Example response:

{
  "fraud_prediction": 1,
  "fraud_probability": 0.91
}

Where:

* fraud_prediction = predicted class (0 or 1)
* fraud_probability = probability of fraud

Input validation is handled using Pydantic schemas to prevent invalid requests.

# 7. Architectural Choices

### Why Handle Class Imbalance?

Fraud datasets are extremely skewed. Techniques like SMOTE help the model learn patterns from minority fraud cases.


### Why Use XGBoost / Tree-Based Models?

* Robust to feature scaling
* Strong performance on tabular data
* Handles nonlinear relationships well


### Why FastAPI?

> Shivam:
* Fast and lightweight
* Automatic OpenAPI documentation
* Built-in request validation
* Excellent for ML inference APIs

### Why Docker?

* Ensures reproducible environments
* Simplifies local development
* Same container can be deployed to cloud infrastructure


### Why uv for Dependency Management?

* Faster dependency resolution
* Deterministic environments
* Lockfile ensures reproducibility

# 8. Project Structure

fraud-detection-api/
│
├── app/
│   ├── main.py        # FastAPI application
│   ├── predictor.py   # Model loading and prediction
│   └── schema.py      # Pydantic input validation
│
├── model/
│   └── fraud_pipeline.pkl
│
├── Credit_Card_Fraud_Detection.ipynb
│
├── Dockerfile
├── pyproject.toml
├── uv.lock
└── README.md


# 9. Running the Project with Docker

### Build the Docker image

docker build -t fraud-detection-api .

### Run the container

docker run -p 8000:8000 fraud-detection-api

### Access API documentation

http://localhost:8000/docs

FastAPI automatically provides an interactive interface for testing the API.


# 10. Cloud Deployment

The Docker image can be deployed to multiple cloud platforms.

### AWS Deployment

Typical production architecture:

Docker Image
↓
Amazon ECR (Container Registry)
↓
Amazon ECS / Fargate
↓
Application Load Balancer
↓
Public API Endpoint


### Google Cloud Run

Steps:

1. Build Docker image
2. Push to Google Container Registry
3. Deploy to Cloud Run

Benefits:

* automatic scaling
* serverless infrastructure
* pay-per-request model


### Render / Railway

For quick portfolio deployments:

1. Push repository to GitHub
2. Connect repository to Render
3. Deploy the Docker service

# 11. Reproducibility

To reproduce this project:

1. Clone the repository
2. Install dependencies with uv
3. Run the FastAPI server or build the Docker image
4. Test the API using /docs

All dependencies are version-locked using:

uv.lock

This ensures consistent environments across machines.

## ✨ Acknowledgments
- Dataset provided by ULB (Université Libre de Bruxelles) via Kaggle.
- Machine learning community for best practices on imbalanced data.

Author: Samiksha Hujare

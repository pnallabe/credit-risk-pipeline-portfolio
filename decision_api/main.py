from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Credit Risk Decision API")

class Borrower(BaseModel):
    annual_income: float
    dti: float
    utilization: float
    inquiries_6m: int
    term_months: int
    fico: int

# placeholder model: replace with MLflow load or joblib
MODEL = None
THRESHOLD = 0.12  # example PD cut-off for approval

def load_model():
    global MODEL
    try:
        MODEL = joblib.load("models/registry/pd_model.joblib")
    except Exception:
        MODEL = None

@app.on_event("startup")
def startup_event():
    load_model()

@app.post("/score")
def score(b: Borrower):
    x = np.array([[b.annual_income, b.dti, b.utilization, b.inquiries_6m, b.term_months, b.fico]])
    if MODEL:
        pd_hat = float(MODEL.predict_proba(x)[0,1])
    else:
        # naive fallback so the demo always runs
        pd_hat = max(0.01, min(0.5, 0.35*b.utilization + 0.02*b.dti - 0.001*b.fico + 0.03*b.inquiries_6m))
    decision = "APPROVE" if pd_hat < THRESHOLD else "REVIEW/DECLINE"
    return {
        "pd": round(pd_hat, 4),
        "decision": decision,
        "policy_threshold": THRESHOLD
    }

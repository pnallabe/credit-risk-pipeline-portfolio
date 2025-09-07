run-api:
\tuvicorn decision_api.main:app --reload --port 8000
train:
\tpython models/training/train_pd.py
drift:
\tpython monitoring/drift_check.py

# Enterprise Credit Risk Pipeline (Portfolio Project)
This project demonstrates how to design and build an enterprise-grade credit risk pipeline that can be applied across multiple lending products — consumer loans, credit cards, SMB lending, and mortgages. It blends credit risk domain expertise with modern data engineering, machine learning, and MLOps practices, making it a showcase of both technical and business skills relevant to financial services and fintech roles.
 
# 🎯 Project Overview: 
Financial institutions rely on robust, scalable, and compliant systems to evaluate credit risk in real-time. This project simulates such a pipeline using open-source datasets and cloud-native tools, while following industry practices around governance, explainability, and monitoring.
 
# 🏗️ Architecture

(see diagrams/pipeline_architecture.py to regenerate this diagram)
Key Layers:
1.	Data Ingestion — Streaming & batch pipelines from internal systems, credit bureau-like datasets, and macroeconomic APIs (Kafka/Kinesis, Python, Airflow/Prefect).
2.	Storage — Data Lake (S3/MinIO) + Warehouse (Redshift/Snowflake/DuckDB).
3.	Data Processing — ETL/ELT with dbt & Spark, plus data quality checks (Great Expectations).
4.	Feature Store — Managed with Feast (DTI, utilization, LTV, cashflow volatility).
5.	Modeling — PD, LGD, EAD models using Logistic Regression & XGBoost; SHAP for explainability.
6.	Decisioning Engine — Risk appetite thresholds, Champion/Challenger rules, pricing adjustments (YAML-driven).
7.	Serving — FastAPI microservice for real-time scoring and decisioning; Streamlit UI demo.
8.	Monitoring & Governance — Drift detection (PSI/KS, AUC), vintage curves, MLflow registry, audit logging, compliance (CECL/IFRS9).
 
# 📊 Datasets Used
This portfolio leverages open datasets to simulate different credit products:
•	Consumer Loans / Credit Cards → LendingClub Loan Data (Kaggle), German Credit (UCI)
•	SMB Lending → SBA PPP Loan Data, Yelp Dataset
•	Mortgages → Fannie Mae Loan Performance Data, Freddie Mac Loan-Level Dataset
•	Macroeconomics → FRED API, World Bank Open Data
 
# ⚙️ Tech Stack
•	Data Engineering → Python, Pandas, dbt, Spark, Airflow/Prefect, Kafka/Kinesis (optional).
•	Storage → S3/MinIO, Redshift/Snowflake, DuckDB.
•	Feature Store → Feast / Tecton.
•	Modeling → scikit-learn, XGBoost, LightGBM, MLflow (model registry).
•	APIs & Serving → FastAPI + Uvicorn, Docker, Kubernetes (demo with Docker Compose).
•	Monitoring & Governance → EvidentlyAI, Grafana/Prometheus, MLflow tracking, audit logs.
 
# 📂 Repository Structure
credit-risk-pipeline/
├─ diagrams/              # Architecture diagrams & matplotlib code
├─ ingestion/             # Data ingestion scripts (LendingClub, PPP, FRED, etc.)
├─ feature_store/         # Feast configs and feature definitions
├─ models/                # Training pipelines for PD, LGD, EAD
├─ decision_api/          # FastAPI scoring & decision service
├─ monitoring/            # Drift detection, model monitoring, dashboards
├─ docs/                  # One-pager & project documentation
├─ app/                   # Streamlit demo UI
├─ requirements.txt       # Dependencies
└─ Makefile               # Quick commands for running & training
 
# 💡 Demo Components
•	Streamlit App → Interactive borrower risk scoring demo.
•	FastAPI Service → REST endpoints for /score, /decision, /explain.
•	Monitoring Report → Drift & performance metrics via Evidently/Grafana.
•	Architecture Diagram → Visual blueprint of the pipeline.
•	One-Page PDF → Executive summary for recruiters & hiring managers.
 
# 🚀 How to Run (Local Demo)
## Clone repo
git clone https://github.com/pnallabe/credit-risk-pipeline.git
cd credit-risk-pipeline

## Install dependencies
pip install -r requirements.txt

## Run ETL / feature prep
make train

## Start API
make run-api

## Open Streamlit demo
streamlit run app/streamlit_demo.py


import pandas as pd
from sklearn.metrics import roc_auc_score
try:
    from evidently.report import Report
    from evidently.metrics import DataDriftPreset
except Exception:
    Report = None

def ks_statistic(scores_ref, scores_cur):
    import numpy as np
    from scipy.stats import ks_2samp
    return ks_2samp(scores_ref, scores_cur).statistic

def run(reference_csv, current_csv, out_html="monitoring_report.html"):
    ref = pd.read_csv(reference_csv)
    cur = pd.read_csv(current_csv)

    if Report:
        report = Report(metrics=[DataDriftPreset()])
        report.run(reference_data=ref, current_data=cur)
        report.save_html(out_html)

    if {"y_true","y_score"} <= set(ref.columns) and {"y_true","y_score"} <= set(cur.columns):
        print("AUC_ref:", roc_auc_score(ref["y_true"], ref["y_score"]))
        print("AUC_cur:", roc_auc_score(cur["y_true"], cur["y_score"]))
        print("KS:", ks_statistic(ref["y_score"], cur["y_score"]))

if __name__ == "__main__":
    run("data/external/ref_scores.csv","data/external/cur_scores.csv")

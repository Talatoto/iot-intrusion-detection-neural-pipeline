import numpy as np
from sklearn.metrics import (
    classification_report, confusion_matrix, roc_auc_score,
    accuracy_score, precision_score, recall_score, f1_score
)
from ..context import Context

def evaluate_model(ctx: Context) -> None:
    model = ctx.model
    X_test = ctx.X_test
    y_test = ctx.y_test.to_numpy() if hasattr(ctx.y_test, "to_numpy") else np.asarray(ctx.y_test)

    y_proba = model.predict(X_test, verbose=0).ravel()
    y_pred = (y_proba >= 0.5).astype(int)

    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    metrics = {
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred, zero_division=0)),
        "recall": float(recall_score(y_test, y_pred, zero_division=0)),
        "f1": float(f1_score(y_test, y_pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_test, y_proba)),
        "confusion_matrix": cm.tolist(),
        "false_positives": int(fp),
        "false_negatives": int(fn),
        "classification_report": classification_report(y_test, y_pred, digits=4),
    }

    print("\n=== Evaluation ===")
    print(metrics["classification_report"])
    print("Confusion matrix:\n", cm)
    print("False Positives (FP):", fp, " Normal predicted as Attack")
    print("False Negatives (FN):", fn, " Attack predicted as Normal (dangerous!)")
    print("ROC-AUC:", round(metrics["roc_auc"], 4))

    ctx.metrics = metrics

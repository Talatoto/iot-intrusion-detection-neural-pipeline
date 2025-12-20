import os
import json
from ..context import Context

def save_artifacts(ctx: Context) -> None:
    cfg = ctx.cfg
    os.makedirs(cfg.out_dir, exist_ok=True)

    # Save metrics
    metrics_path = os.path.join(cfg.out_dir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(ctx.metrics, f, indent=2)
    print(f"Saved metrics -> {metrics_path}")

    # Save training history
    hist = ctx.history.history if ctx.history is not None else {}
    history_path = os.path.join(cfg.out_dir, "train_history.json")
    with open(history_path, "w", encoding="utf-8") as f:
        json.dump(hist, f, indent=2)
    print(f"Saved training history -> {history_path}")

    # Save model
    model_path = os.path.join(cfg.out_dir, "ids_model.keras")
    ctx.model.save(model_path)
    print(f"Saved model -> {model_path}")

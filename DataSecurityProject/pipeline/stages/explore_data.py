import os
import json
from ..context import Context

def explore_data(ctx: Context) -> None:
    df = ctx.df
    cfg = ctx.cfg

    print("Dataset shape:", df.shape)
    print("\nColumns:\n", df.columns.tolist())

    missing = df.isna().sum().sort_values(ascending=False)
    print("\nMissing values (top 15):")
    print(missing.head(15))

    # Attack categories 
    if cfg.attack_col in df.columns:
        print("\nAttack distribution:")
        print(df[cfg.attack_col].value_counts())

    if cfg.attack_subtype_col in df.columns:
        print("\nAttack subtype distribution (top 10):")
        print(df[cfg.attack_subtype_col].value_counts().head(10))

    if cfg.label_col in df.columns:
        print("\nBinary label distribution:")
        print(df[cfg.label_col].value_counts())

    # Save a small summary forreport
    summary = {
        "shape": list(df.shape),
        "columns": df.columns.tolist(),
        "missing_top15": missing.head(15).to_dict(),
        "attack_distribution": df[cfg.attack_col].value_counts().to_dict()
        if cfg.attack_col in df.columns else None,
        "attack_subtype_top10": df[cfg.attack_subtype_col].value_counts().head(10).to_dict()
        if cfg.attack_subtype_col in df.columns else None,
        "label_distribution": df[cfg.label_col].value_counts().to_dict()
        if cfg.label_col in df.columns else None,
    }

    out_path = os.path.join(cfg.out_dir, "dataset_summary.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"\nSaved dataset summary -> {out_path}")

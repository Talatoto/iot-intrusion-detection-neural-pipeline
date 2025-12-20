import pandas as pd
from sklearn.model_selection import train_test_split
from ..context import Context
#build
def build_dataset(ctx: Context) -> None:
    df = ctx.df.copy()
    cfg = ctx.cfg

    # Remove duplicate records 
    df = df.drop_duplicates()

    # Ensure required cols exist
    for col in [cfg.label_col, cfg.attack_col, cfg.attack_subtype_col]:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Target
    y = df[cfg.label_col].astype(int)

    # Drop leakage columns 
    X = df.drop(columns=[cfg.label_col, cfg.attack_col, cfg.attack_subtype_col])

    # Stratified sampling by label to avoid memory issues
    tmp = pd.concat([X, y.rename(cfg.label_col)], axis=1)
    tmp = tmp.groupby(cfg.label_col, group_keys=False).apply(
        lambda g: g.sample(min(len(g), cfg.sample_per_class), random_state=cfg.seed)
    )

    y = tmp[cfg.label_col].astype(int)
    X = tmp.drop(columns=[cfg.label_col])

    print("\nAfter sampling:", X.shape)
    print("Sampled label distribution:\n", y.value_counts())

    # Split train/test
    ctx.X_train_raw, ctx.X_test_raw, ctx.y_train, ctx.y_test = train_test_split(
        X, y,
        test_size=cfg.test_size,
        random_state=cfg.seed,
        stratify=y
    )

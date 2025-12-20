import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from ..context import Context


def preprocess_fit_transform(ctx: Context) -> None:
    X_train_raw = ctx.X_train_raw
    X_test_raw = ctx.X_test_raw

    # Identify types from TRAIN only
    cat_cols = X_train_raw.select_dtypes(include=["object"]).columns.tolist()
    num_cols = X_train_raw.select_dtypes(include=[np.number]).columns.tolist()

    print("\nNumeric cols:", len(num_cols))
    print("Categorical cols:", len(cat_cols), cat_cols)

    preprocess = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=True), cat_cols),
        ],
        remainder="drop"
    )

    X_train = preprocess.fit_transform(X_train_raw)
    X_test = preprocess.transform(X_test_raw)

    # Convert to dense ONLY if sparse
    if hasattr(X_train, "toarray"):
        X_train = X_train.toarray()
    if hasattr(X_test, "toarray"):
        X_test = X_test.toarray()

    ctx.X_train = X_train
    ctx.X_test = X_test
    ctx.preprocess = preprocess

    print("\nFinal shapes:")
    print("X_train:", ctx.X_train.shape, "X_test:", ctx.X_test.shape)

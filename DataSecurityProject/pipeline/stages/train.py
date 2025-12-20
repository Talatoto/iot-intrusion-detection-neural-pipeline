import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping
from ..context import Context

def train_model(ctx: Context) -> None:
    cfg = ctx.cfg

    X_train = ctx.X_train
    y_train = ctx.y_train.to_numpy() if hasattr(ctx.y_train, "to_numpy") else np.asarray(ctx.y_train)

    tf.random.set_seed(cfg.seed)
    np.random.seed(cfg.seed)

    model = Sequential([
        Dense(256, activation="relu", input_shape=(X_train.shape[1],)),
        BatchNormalization(),
        Dropout(0.30),

        Dense(128, activation="relu"),
        BatchNormalization(),
        Dropout(0.30),

        Dense(64, activation="relu"),
        Dropout(0.20),

        Dense(1, activation="sigmoid")
    ])

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=cfg.lr),
        loss="binary_crossentropy",
        metrics=[
            tf.keras.metrics.BinaryAccuracy(name="accuracy"),
            tf.keras.metrics.Precision(name="precision"),
            tf.keras.metrics.Recall(name="recall"),
            tf.keras.metrics.AUC(name="auc"),
        ]
    )

    history = model.fit(
        X_train, y_train,
        validation_split=cfg.val_split,
        epochs=cfg.epochs,
        batch_size=cfg.batch_size,
        callbacks=[EarlyStopping(patience=cfg.early_stop_patience, restore_best_weights=True)],
        verbose=1
    )

    ctx.model = model
    ctx.history = history

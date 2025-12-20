from dataclasses import dataclass
from typing import Any, Optional, Dict
import pandas as pd
from .config import Config

@dataclass
class Context:
    cfg: Config

    # Raw full dataframe
    df: Optional[pd.DataFrame] = None

    # Train/test splits (raw)
    X_train_raw: Any = None
    X_test_raw: Any = None
    y_train: Any = None
    y_test: Any = None

    # Preprocessing + transformed
    preprocess: Any = None
    X_train: Any = None
    X_test: Any = None

    # Model + results
    model: Any = None
    history: Any = None
    metrics: Optional[Dict[str, Any]] = None


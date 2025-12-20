import os
import pandas as pd
from ..context import Context

def load_data(ctx: Context) -> None:
    cfg = ctx.cfg
    os.makedirs(cfg.out_dir, exist_ok=True)

    ctx.df = pd.read_csv(cfg.csv_path)

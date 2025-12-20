from pipeline.config import Config
from pipeline.context import Context
from pipeline.runner import Stage, run_pipeline

from pipeline.stages.load_data import load_data
from pipeline.stages.explore_data import explore_data
from pipeline.stages.build_dataset import build_dataset
from pipeline.stages.preprocess import preprocess_fit_transform
from pipeline.stages.train import train_model
from pipeline.stages.evaluate import evaluate_model
from pipeline.stages.save_artifacts import save_artifacts

if __name__ == "__main__":
    cfg = Config(
        csv_path=r"C:\Users\Tala\Downloads\BoTNeTIoT-L01-v2.csv",  
        out_dir="artifacts",
        sample_per_class=200_000
    )
    ctx = Context(cfg=cfg)

    stages = [
        Stage("load", load_data, deps=[]),
        Stage("explore", explore_data, deps=["load"]),
        Stage("build", build_dataset, deps=["load"]),
        Stage("preprocess", preprocess_fit_transform, deps=["build"]),
        Stage("train", train_model, deps=["preprocess"]),
        Stage("evaluate", evaluate_model, deps=["train"]),
        Stage("save", save_artifacts, deps=["train", "evaluate"]),
    ]

    run_pipeline(ctx, stages)

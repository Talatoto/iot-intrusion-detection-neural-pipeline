from dataclasses import dataclass

@dataclass
class Config:
    # Path to dataset
    csv_path: str

    # Output directory
    out_dir: str = "artifacts"

    # Dataset columns
    label_col: str = "label"
    device_col: str = "Device_Name"
    attack_col: str = "Attack"
    attack_subtype_col: str = "Attack_subType"

    # Sampling / splitting
    sample_per_class: int = 200_000
    test_size: float = 0.2
    seed: int = 42

    # Training hyperparameters
    lr: float = 1e-3
    batch_size: int = 256
    epochs: int = 25
    val_split: float = 0.2
    early_stop_patience: int = 4

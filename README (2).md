# Pipeline-Based Neural Network Intrusion Detection System (IDS) for IoT Networks

## Project Information
**Course:** Data Security / Network Security  
**Project Type:** Course Project  

**Developed by:**  
- Student 1: Tala  
- Student 2: (Second Student Name)  

---

## Project Presentation
A visual presentation explaining the system design, dataset, pipeline architecture, and evaluation results is available at:

https://prezi.com/view/2WDORkAi3uZDGXWDRdRE/?referral_token=UIuwjrlnB3FN

---

## Project Overview
This project implements a **pipeline-based Intrusion Detection System (IDS)** using a **neural network** to detect malicious traffic in **IoT networks**.

The system follows a **modular, dependency-driven pipeline architecture**, where each stage of the machine learning workflow is implemented as a separate component and executed only when its dependencies are satisfied.

The IDS performs **binary classification**, identifying traffic as either:
- **Normal traffic**
- **Attack traffic**

---

## Project Objectives
- Detect malicious IoT network traffic using machine learning
- Design a clean and modular pipeline-based system
- Handle large-scale datasets efficiently
- Prevent data leakage during model training
- Evaluate performance using security-relevant metrics

---

## Project Structure

```
DataSecurityProject/
│
├── main.py
├── pipeline/
│   ├── config.py
│   ├── context.py
│   ├── runner.py
│   └── stages/
│       ├── load_data.py
│       ├── explore_data.py
│       ├── build_dataset.py
│       ├── preprocess.py
│       ├── train.py
│       ├── evaluate.py
│       └── save_artifacts.py
│
└── artifacts/
```

---

## File-by-File Explanation

### main.py
- Entry point of the project
- The only file that should be executed
- Creates the configuration and shared context
- Defines pipeline stages and their dependencies
- Starts pipeline execution

### pipeline/config.py
- Stores configuration parameters such as dataset path, column names, and hyperparameters
- Centralizes configuration for reproducibility

### pipeline/context.py
- Shared memory object used by all pipeline stages
- Stores datasets, features, models, and evaluation results

### pipeline/runner.py
- Controls pipeline execution
- Resolves stage dependencies
- Ensures correct execution order

---

## Pipeline Stages

### load_data.py
- Loads the dataset from disk
- Initializes output directories

### explore_data.py
- Performs dataset exploration
- Displays dataset size, feature information, and class distributions
- Saves dataset summary for reporting

### build_dataset.py
- Removes duplicate records
- Creates the target label
- Drops attack name columns to prevent label leakage
- Applies stratified sampling
- Splits data into training and testing sets

### preprocess.py
- Encodes categorical features
- Scales numerical features
- Fits preprocessing only on training data
- Prepares data for neural network input

### train.py
- Defines and trains the neural network model
- Uses dense layers, batch normalization, and dropout
- Stores the trained model and training history

### evaluate.py
- Evaluates model performance on test data
- Computes accuracy, precision, recall, F1-score, ROC-AUC, and confusion matrix
- Analyzes false positives and false negatives

### save_artifacts.py
- Saves metrics, training history, and trained model to disk

---

## Pipeline Execution Flow

```
load_data
    ↓
explore_data
    ↓
build_dataset
    ↓
preprocess
    ↓
train
    ↓
evaluate
    ↓
save_artifacts
```

---

## Dataset Description
- Large-scale IoT network traffic dataset
- Over 7 million records
- Flow-based statistical features
- Binary label:
  - 0 → Normal traffic
  - 1 → Attack traffic

Stratified sampling is applied to handle dataset scale.

---

## Attack Types in the Dataset

### Attack Families
- **Mirai** – IoT botnet exploiting weak credentials, primarily used for DDoS attacks
- **Gafgyt (Bashlite)** – Linux-based IoT botnet used for flooding and scanning attacks

### Attack Subtypes
- UDP Flood
- TCP Flood
- SYN Flood
- ACK Flood
- Port Scanning
- Combo Attacks
- Junk Traffic

Attack name columns are removed before training to prevent data leakage.

---

## Neural Network Model
- Fully connected feedforward neural network
- ReLU activation functions
- Batch normalization and dropout for regularization
- Sigmoid output layer for binary classification

---

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

Recall is the most critical metric for intrusion detection systems.

---

## Outputs
After running the pipeline, the following files are saved in the artifacts directory:
- dataset_summary.json
- metrics.json
- train_history.json
- ids_model.keras

---

## How to Run the Project

```bash
pip install pandas numpy scikit-learn tensorflow
python main.py
```

---

## Conclusion
This project demonstrates a robust, modular, and reproducible Intrusion Detection System for IoT networks using neural networks. The pipeline-based architecture ensures clean separation of concerns, prevents data leakage, and enables security-focused evaluation.

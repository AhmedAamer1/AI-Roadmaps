from pathlib import Path

repos = {
    "Melanoma-Detection-Xception-XAI": {
        "description": "Explainable deep learning for early melanoma detection using Xception, Optuna, and XAI techniques.",
        "folders": [
            "images",
            "models"
        ]
    },

    "Wind-Turbine-Anomaly-Detection": {
        "description": "Early fault detection in wind turbines using 1D-CNN and CNN-LSTM-Attention on multi-source SCADA data.",
        "folders": [
            "images",
            "models"
        ]
    },

    "Badminton-App-Data-Analysis": {
        "description": "Exploratory and business analytics for a badminton mobile application.",
        "folders": [
            "data",
            "images"
        ]
    }
}


def create_readme(repo_name, description):
    return f"""# {repo_name}

## Overview

{description}

---

## Project Structure

```text
.
├── notebook.ipynb
├── requirements.txt
├── README.md
├── images
└── models
```

---

## Features

- Data preprocessing
- Model training
- Evaluation
- Visualization

---

## Results

Coming soon...

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Future Work

- Improve performance
- Add more experiments
- Deploy the model

"""


for repo, info in repos.items():

    base = Path(repo)
    base.mkdir(exist_ok=True)

    # folders
    for folder in info["folders"]:
        (base / folder).mkdir(exist_ok=True)

    # files
    (base / "notebook.ipynb").touch()
    (base / "requirements.txt").touch()

    with open(base / "README.md", "w", encoding="utf-8") as f:
        f.write(create_readme(repo, info["description"]))

print("Repositories created successfully!")
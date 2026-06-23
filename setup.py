import os
import subprocess

# ==========================
# Folder Structure
# ==========================
structure = {
    "Beginner-Level": [
        "01-Python",
        "02-Mathematics",
        "03-Numpy-Pandas",
        "04-Machine-Learning",
        "05-Scikit-Learn",
        "Projects"
    ],
    "Intermediate-Level": [
        "01-Deep-Learning",
        "02-Computer-Vision",
        "03-NLP",
        "04-MLOps",
        "05-Generative-AI",
        "Projects"
    ]
}

# ==========================
# Create folders and README files
# ==========================
for level, folders in structure.items():
    for folder in folders:
        path = os.path.join(level, folder)
        os.makedirs(path, exist_ok=True)

        readme_path = os.path.join(path, "README.md")

        if not os.path.exists(readme_path):
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(f"# {folder}\n")

# Root README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(
"""# AI Roadmaps 🚀

A complete roadmap for learning Artificial Intelligence from scratch.

## Beginner Level
- Python
- Mathematics
- NumPy & Pandas
- Machine Learning
- Scikit-Learn

## Intermediate Level
- Deep Learning
- Computer Vision
- NLP
- MLOps
- Generative AI

⭐ Star this repository if it helps you!
"""
    )

print("Project structure created successfully.")

# ==========================
# Git Commands
# ==========================
commands = [
    ["git", "add", "."],
    ["git", "commit", "-m", "Initial AI Roadmaps structure"],
    ["git", "branch", "-M", "main"],
    ["git", "push", "-u", "origin", "main"]
]

for cmd in commands:
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print(f"Failed: {' '.join(cmd)}")

print("Done!")
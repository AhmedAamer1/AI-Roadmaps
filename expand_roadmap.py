from pathlib import Path

roadmaps = {
    "Beginner-Level": {
        "01-Python": {
            "courses": [
                ("CS50P", "https://cs50.harvard.edu/python/"),
                ("Python for Everybody", "https://www.coursera.org/specializations/python")
            ],
            "projects": [
                "Calculator",
                "To-Do App",
                "Student Management System"
            ]
        },

        "02-Mathematics": {
            "courses": [
                ("Mathematics for Machine Learning",
                 "https://www.coursera.org/specializations/mathematics-machine-learning"),
                ("StatQuest",
                 "https://www.youtube.com/@statquest"),
                ("Khan Academy Statistics",
                 "https://www.khanacademy.org/math/statistics-probability"),
                ("3Blue1Brown Calculus",
                 "https://www.3blue1brown.com/topics/calculus")
            ],
            "projects": [
                "Linear Algebra Exercises",
                "Probability Problems"
            ]
        },

        "03-Numpy-Pandas": {
            "courses": [
                ("Kaggle Pandas",
                 "https://www.kaggle.com/learn/pandas"),
                ("NumPy Documentation",
                 "https://numpy.org/doc/stable/"),
                ("Pandas Documentation",
                 "https://pandas.pydata.org/docs/"),
                ("FreeCodeCamp Data Analysis",
                 "https://www.freecodecamp.org/learn/data-analysis-with-python/")
            ],
            "projects": [
                "Exploratory Data Analysis",
                "Sales Analysis"
            ]
        },

        "04-Machine-Learning": {
            "courses": [
                ("Machine Learning Specialization",
                 "https://www.coursera.org/specializations/machine-learning-introduction"),
                ("Scikit-Learn Documentation",
                 "https://scikit-learn.org/stable/")
            ],
            "projects": [
                "House Price Prediction",
                "Customer Churn Prediction",
                "Loan Approval Prediction"
            ]
        },

        "05-Scikit-Learn": {
            "courses": [
                ("Scikit-Learn Official Docs",
                 "https://scikit-learn.org/stable/")
            ],
            "projects": [
                "End-to-End ML Pipeline"
            ]
        }
    },

    "Intermediate-Level": {

        "01-Deep-Learning": {
            "courses": [
                ("Deep Learning Specialization",
                 "https://www.coursera.org/specializations/deep-learning"),
                ("Learn PyTorch",
                 "https://www.learnpytorch.io/")
            ],
            "projects": [
                "ANN Classifier",
                "Image Classification"
            ]
        },

        "02-Computer-Vision": {
            "courses": [
                ("Learn PyTorch Computer Vision",
                 "https://www.learnpytorch.io/"),
                ("Ultralytics YOLO Docs",
                 "https://docs.ultralytics.com/")
            ],
            "projects": [
                "Cat vs Dog Classifier",
                "Face Mask Detection"
            ]
        },

        "03-NLP": {
            "courses": [
                ("Hugging Face NLP Course",
                 "https://huggingface.co/learn/nlp-course"),
                ("Transformers Documentation",
                 "https://huggingface.co/docs/transformers/index")
            ],
            "projects": [
                "Sentiment Analysis",
                "Text Classification",
                "Chatbot"
            ]
        },

        "04-MLOps": {
            "courses": [
                ("Made With ML",
                 "https://madewithml.com/"),
                ("MLflow Documentation",
                 "https://mlflow.org/docs/latest/index.html"),
                ("DVC Documentation",
                 "https://dvc.org/doc")
            ],
            "projects": [
                "Model Deployment API",
                "ML Pipeline"
            ]
        },

        "05-Generative-AI": {
            "courses": [
                ("LangChain Academy",
                 "https://academy.langchain.com/"),
                ("LangChain Docs",
                 "https://python.langchain.com/docs/introduction/"),
                ("OpenAI API Docs",
                 "https://platform.openai.com/docs/overview")
            ],
            "projects": [
                "PDF Chatbot",
                "AI Assistant",
                "RAG System"
            ]
        }
    }
}


def create_module_files(base, module, data):

    folder = Path(base) / module

    # README
    with open(folder / "README.md", "w", encoding="utf-8") as f:
        f.write(f"# {module}\n\n")
        f.write("## Resources\n\n")

        for course, link in data["courses"]:
            f.write(f"- [{course}]({link})\n")

        f.write("\n## Projects\n\n")

        for project in data["projects"]:
            f.write(f"- {project}\n")

    # Resources.md
    with open(folder / "Resources.md", "w", encoding="utf-8") as f:
        f.write("# Resources\n\n")

        for course, link in data["courses"]:
            f.write(f"- [{course}]({link})\n")

    # Projects.md
    with open(folder / "Projects.md", "w", encoding="utf-8") as f:
        f.write("# Projects\n\n")

        for project in data["projects"]:
            f.write(f"- {project}\n")

    # Checklist.md
    with open(folder / "Checklist.md", "w", encoding="utf-8") as f:
        f.write("# Checklist\n\n")

        for course, _ in data["courses"]:
            f.write(f"- [ ] Finish {course}\n")

        for project in data["projects"]:
            f.write(f"- [ ] Build {project}\n")


for level, modules in roadmaps.items():
    for module, info in modules.items():
        create_module_files(level, module, info)

print("AI Roadmap expanded successfully!")
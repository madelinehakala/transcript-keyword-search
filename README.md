# Transcript Keyword Search App

## Overview
This repository houses a basic Streamlit app to perform keyword search over call center 
transcripts. The goal is to provide stakeholders with a simple, efficient method to identify 
relevant calls as they perform QA, conduct performance reviews of employees, etc.

## Repository Structure
```
├── .github/  # GitHub-specific files (actions, workflows, etc.)
│   └── workflows/  # GitHub Actions workflows
│       └── ruff.yml  # Ruff check configuration
├── app/ # Application
│   ├── demo_inputs/ # Demo input examples
│   |   └── example_transcripts.py
│   ├── helper_functions/ # Helper functions called in main.py
│   |   └── keyword_search.py
│   └── main.py  # Main Streamlit app entrypoint
├── .gitignore  # Files ignored by version control
├── poetry.lock  # Dependencies
├── pyproject.toml  # Build system requirements
└── README.md  # Project overview
```

## Environment Setup
*This project uses a Poetry virtual environment.*

**1. Install Poetry (if you have not already).**
```
pipx install poetry==1.8.4
```

**2. Create the virtual environment with the necessary packages and dependencies.**
```
poetry install
```

**3. Initialize the environment.**
```
poetry shell
```
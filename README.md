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

To set up the environment for the first time, run the following commands:

**1. Install Poetry (if you have not already).**
```
pipx install poetry==1.8.4
```

**2. Create the virtual environment with the necessary packages and dependencies.**
```
poetry install
```

## Running the Streamlit App
To run the Streamlit app, run the following commands:

**1. Initialize the environment.**
```
poetry shell
```

**2. Move to the correct directory.**
```
cd app
```

**3. Run the app.**
```
streamlit run main.py
```

**4. Exit the app when finished.**
```
[Ctrl+C]
```

**5. Exit the Poetry environment.**
```
exit
```

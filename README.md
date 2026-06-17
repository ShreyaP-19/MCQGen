# MCQ Generator

A Streamlit app that generates multiple-choice questions from PDF or TXT content using OpenAI and LangChain.

## Features

- Upload a PDF or text file.
- Generate a custom number of MCQs.
- Specify subject and tone/complexity level.
- Display quiz results in a table with choices and correct answers.
- Provide a short review of the generated quiz.

## Prerequisites

- Python 3.11
- `OPENAI_API_KEY` from OpenAI

## Installation

1. Create and activate a virtual environment:

```powershell
python -m venv env
.\env\Scripts\Activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
pip install -e .
```

3. Create a `.env` file in the project root with your OpenAI key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the app

```powershell
streamlit run StreamlitApp.py
```

Then open the local Streamlit URL shown in the terminal.

## Usage

- Upload a PDF or TXT file.
- Enter the number of MCQs to generate.
- Enter a subject name.
- Enter a tone or complexity level (for example: "Simple", "Intermediate", "Advanced").
- Click **Generate MCQs**.

## Project structure

- `StreamlitApp.py` — main Streamlit application entry point.
- `src/mcqgenerator/MCQGenerator.py` — LangChain/OpenAI quiz generation logic.
- `src/mcqgenerator/utils.py` — helpers for reading files and formatting output.
- `requirements.txt` — Python package dependencies.
- `setup.py` — package installation configuration.
- `Response.json` — response format guide used by the generator.

## Supported file types

- `.pdf`
- `.txt`

## Notes

- The app uses OpenAI via the `langchain` and `langchain_openai` packages.
- `Response.json` is used to guide the output schema for generated quizzes.
- Ensure `env` and `.env` are excluded from source control (already listed in `.gitignore`).

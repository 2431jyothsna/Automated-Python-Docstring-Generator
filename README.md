# Automated-Python-Docstring-Generator

## Overview

Docstring Generator is a Python-based tool that automatically generates docstrings for Python functions and classes. It analyzes the structure of Python code using AST (Abstract Syntax Tree) and creates meaningful documentation to improve code readability and maintainability.

This project provides a simple interface where users can upload a Python file and receive automatically generated docstrings.

---

## Features

* Automatic docstring generation for Python functions and classes
* Code analysis using Python AST
* Streamlit-based user interface
* Upload Python files and preview code
* Generate documentation instantly
* Clean and modular backend architecture

---

## Project Structure

```
DOCSTRING_GENERATOR
│
├── backend
│   ├── analyzer
│   │   └── ast_parser.py
│   ├── cli
│   │   └── commands.py
│   ├── core
│   │   └── synthesis_engine.py
│   ├── ui
│   │   └── streamlit_ui.py
│   ├── utils
│   │   └── helpers.py
│   ├── validator
│   │   └── quality.py
│   ├── app.py
│   |___test.py
|   |___requirements.txt
│   |
│   └── .env
│__sample.py
|__MIT license
├── README.md
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/docstring-generator.git
cd docstring-generator
```

### 2. Create a virtual environment

```
python -m venv venv
```

### 3. Activate the environment

Windows:

```
venv\Scripts\activate
```

Linux / Mac:

```
source venv/bin/activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Navigate to the backend folder:

```
cd backend
```

Run the Streamlit application:

```
streamlit run app.py
```

Open your browser and go to:

```
http://localhost:8501
```

---

## Usage

1. Open the Streamlit application.
2. Upload a Python `.py` file.
3. The uploaded code will be displayed in the interface.
4. Click **Generate Docstrings**.
5. The system will analyze the code and generate documentation.

---

## Technologies Used

* Python
* Streamlit
* Abstract Syntax Tree (AST)
* Modular Python architecture

---

## Example Input

```
def add(a, b):
    return a + b
```

Example Output:

```
def add(a, b):
    """
    Adds two numbers and returns the result.

    Args:
        a (int/float): First number
        b (int/float): Second number

    Returns:
        int/float: Sum of the two numbers
    """
    return a + b
```

---

## Future Improvements

* Support for multiple docstring styles (Google, NumPy, reStructuredText)
* Batch processing of Python files
* Integration with code editors
* Download generated files

---

## Author

Jyothsna

---

## License

This project is open-source and available under the MIT License.

# Project Title

## 🌐 URL

```bash
https://example.com
```

## 📖 Project Description

Project Description

## 🖥️ Tech Stack

- 📦 Conda
- ⚙️ Make
- 🐍 Python
- 🧪 Pytest
- 🧹 Ruff

## ⚙️ Installation

Clone this repository

```bash
git clone git@github.com:username/project_template.git
cd project_template
```

Create a environment:

Use Conda or uv

```bash
conda create -n project_template python=3.10
or
uv venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -e .
or
uv pip install -e .
```

Install make for makefile:

```bash
conda install -c conda-forge make
or
uv pip install make
```

## ▶️ Run the Project

Activate your environment:

```bash
conda activate project_name
```

Run the main scraper:

```bash
python src/project_template/main.py
```

## ✅ Before Commit

Run tests:

```bash
pytest
```

Apply Ruff linter:

```bash
ruff check .
```

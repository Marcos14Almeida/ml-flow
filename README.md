# MLFlow

## 🌐 URL

```bash
https://example.com
```

## 📖 Project Description

Project Description

## 🖥️ Tech Stack

- 📦 UV
- ⚙️ Make
- 🐍 Python
- 🧪 Pytest
- 🧹 Ruff

## 🗂️ Folder Structure

```bash
ml-flow/
├── data/
│   └── sample.csv
├── assets/
│   └── emojis.md
├── src/
│   └── ml_flow_mrc/
│       ├── core/
│       │   └── business_logic.py
│       ├── utils/
│       │   ├── app_loger.py
│       ├── config.py
│       └── main.py
├── tests/
│   └── test_main.py
├── pyproject.toml
├── README.md
├── Makefile
└── TODO
```

## ⚙️ Installation

Clone this repository

```bash
git clone git@github.com:username/ml-flow.git
cd ml-flow
```

Create a environment:

Use Conda or uv

```bash
conda create -n ml-flow python=3.10
conda activate ml-flow
or
uv venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -e .
or
uv pip install -e .
uv pip install -e .[dev]
```

Install make for makefile:

```bash
conda install -c conda-forge make
```

## ▶️ Run the Project

Activate your environment:

```bash
conda activate ml-flow
or
.venv\Scripts\activate
```

Run the main scraper:

```bash
python src/ml_flow_mrc/main.py
```

```bash
mlflow ui
```

## ✅ Tests

Run tests:

```bash
pytest
```

## ✅ Linter

Apply Ruff linter:

```bash
ruff check .
```

## ✅ Mypy

Apply mypy linter:

```bash
uv run mypy src
```

## ✅ Full Debug

```bash
pytest && ruff check . && uv run mypy src
```

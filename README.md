# CodeRefinery Day 2 starter

This is a small Python project for a teaching session on testing, Git workflows, pull requests, CI, and basic project documentation. The goal is to practice a minimal but realistic development workflow in a repository that is easy to understand and verify.

## Project purpose

The project is designed to help learners:

- write and run simple Python functions
- test expected behavior with `pytest`
- understand the difference between local validation and automated checks
- use Git branches and pull requests in a simple collaborative workflow
- see how a minimal GitHub Actions workflow checks code before it is merged

## File structure

The repository is intentionally small and focused:

- `example.py`: a simple Python file with arithmetic functions and tests
- `requirements-dev.txt`: development dependencies used for local test execution
- `.github/workflows/ci.yml`: GitHub Actions workflow for automated checks
- `LICENSE`: the project license
- `README.md`: project overview and setup instructions

## Prepare Python and a virtual environment on Windows with Git Bash

Make sure Git and Python 3.13 are installed. Then open Git Bash in the project folder and run:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements-dev.txt
```

This creates an isolated virtual environment and installs the test dependency needed for the project.

## Install dependencies

From the project root:

```bash
python -m pip install -r requirements-dev.txt
```

This installs `pytest`, which is used to run the checks in the repository.

## Run the tests for this project

To run the project tests from the repository root, use:

```bash
python -m pytest -v example.py
```

This is the exact command used by the repository's CI workflow and matches the current project structure.

## Simple CI workflow

The project includes a GitHub Actions workflow in `.github/workflows/ci.yml`.

The current workflow is intentionally simple:

- runs on `ubuntu-latest`
- checks out the repository
- sets up Python 3.13
- installs dependencies from `requirements-dev.txt`
- runs:

```bash
python -m pytest -v example.py
```

The workflow is configured with:

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:
```

This means that a push directly to `main` triggers the check, and a pull request targeting `main` also triggers it. A standard push to a feature branch without opening a pull request does not trigger the workflow under the current filter.

## How to open and check CI results

After pushing or creating a pull request:

1. Open the GitHub repository.
2. Click the `Actions` tab.
3. Select the latest workflow run.
4. Open the job named `tests`.
5. Review the log output to confirm whether the checks passed or failed.

This is the fastest way to see whether the project still passes its automated validation.

## License and sources

This teaching adaptation is distributed under the [MIT](LICENSE) license.

It follows the learning pattern of [CodeRefinery testing](https://coderefinery.github.io/testing/) and [full-cycle collaboration](https://coderefinery.github.io/testing/full-cycle-ci/).

Prepared with AI assistance; the local test checkpoints were checked separately.

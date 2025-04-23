# Usage

To calculate the stem volumes of data provided in a CSV file, use the command

    $ uv run stem-volumes path/to/file.csv /path/to/output/file.csv

# Setup

This project uses [uv](https://github.com/astral-sh/uv) for software dependency
management. It will set up a venv in the folder `.venv` when you use the `uv`
command. For developing you need to install the `uv` tool. You can find its
documentation for installing and usage at https://docs.astral.sh/uv/.

# Testing

The project uses the [pytest](https://pytest.org/) for testing.
You can run the available tests by

    $ uv run pytest

# Code Formatting

To check for code formatting issues, run

    $ uv run ruff format --check

# Code Linting

To check for linting issues, run

    $ uv run ruff check

# Documentation

For documentation generation [pdoc3](https://pdoc3.github.io/pdoc/) is used.
To generate the documentation in the `docs/` folder, run

    $ uv run pdoc --html -o docs/ src/stem_volumes

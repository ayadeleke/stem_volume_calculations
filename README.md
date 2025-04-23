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

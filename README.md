<div align="center">

# FastAPI Project Template with Loguru

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Formatted with: isort](https://img.shields.io/badge/formatted%20with-isort-blue.svg)](https://pycqa.github.io/isort/)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Tested with pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC.svg)](https://docs.pytest.org/en/stable/)

</div>

## About 📘

This repository serves as a template for a **minimal FastAPI project** with enhanced logging using **Loguru**. It's managed with **Poetry** for efficient dependency resolution, ensuring a robust and maintainable codebase.

## Features 🌟

- **FastAPI Framework**: Utilizes the latest FastAPI framework for high performance and ease of development.
- **Loguru Integration**: Includes pre-configured Loguru for superior logging capabilities.
- **Poetry for Dependency Management**: Employs Poetry to simplify package management and dependency resolution.
- **Black Code Style**: Adheres to the Black code style for consistent and clean Python code.
- **isort for Import Sorting**: Ensures imports are neatly organized and consistent using isort.
- **mypy for Static Type Checking**: Incorporates mypy to catch errors and ensure type safety in your codebase.
- **pytest for Testing**: Leverages pytest for comprehensive and efficient testing of your application.
- 

## Usage 🛠️

To use this template, simply press the button on GitHub to create a new repository based on this template.
Next, rename the project and docker image in following files
- [`pyproject.toml`](pyproject.toml)
- [`docker-compose.yml`](docker-compose.yml)
- [`.github/workflows/build-docker-image-release.yml`](.github/workflows/build-docker-image-release.yml)
  - **and uncomment the `on` section in this file for it to work**

## Installation 💻

```shell
poetry install
```

## Running 🏃‍♂️

```shell
poetry shell
poetry run app
```

## Troubleshooting 🔍

For any issues or troubleshooting queries, please refer to the [Issues section](https://github.com/barabum0/fastapi-template/issues) of this GitHub repository.

## Contribution 👥

Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

## License 📜

This project is open-sourced under the [MIT License](LICENSE).
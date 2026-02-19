# sahim-django-common 📦

**Django utilities and common components** developed and maintained by [SahimCo](https://github.com/sahimco). This package is published publicly on [PyPI](https://pypi.org/project/sahim-django-common/) for use in any Django project.

## 📥 Installation

Install from PyPI with pip:

```bash
pip install sahim-django-common
```

Or add to your project's dependencies (e.g. `requirements.txt`):

```
sahim-django-common
```

## 📋 Requirements

- Python 3.10+
- Django 5.0+

## 🚀 Usage

Add the app to your Django project's `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    "sahim_django_common",
    # ...
]
```

Or with the full app config:

```python
INSTALLED_APPS = [
    # ...
    "sahim_django_common.apps.SahimDjangoCommonConfig",
    # ...
]
```

After installation, follow the documentation for the specific utilities you need. Usage details will depend on which modules you use.

*(Documentation for individual utilities will be added here or in the docs as the package grows.)*

## 📦 What's included

This package provides reusable Django utilities used across SahimCo projects, such as:

- 🔧 Helper functions and decorators
- ⚡ Optional management commands and app hooks

*(This section can be updated as new utilities are added.)*

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🔧 Development

### Setup

Install the package in editable mode with all dev and test dependencies:

```bash
pip install -r requirements-dev.txt
```

This installs the package (editable) plus pre-commit, pytest, and pytest-django.

### Pre-commit

This project uses [pre-commit](https://pre-commit.com/) for code quality checks:

```bash
# Install git hooks (run once)
pre-commit install
```

Hooks run automatically on commit. To run manually:

```bash
pre-commit run --all-files
```

### Tests

Run tests with pytest:

```bash
pytest
```

## 📤 Publishing releases (PyPI)

Releases are published to PyPI automatically via GitHub Actions when you push a version tag.

### One-time setup: Trusted Publishing on PyPI

1. Log in to [PyPI](https://pypi.org) and open your project’s **Publishing** settings:
   - `https://pypi.org/manage/project/sahim-django-common/settings/publishing/`
1. Add a **Trusted Publisher** with:
   - **Owner:** `sahimco` (or your GitHub org/user)
   - **Repository name:** `sahim-django-common`
   - **Workflow name:** `release.yml`
   - **Environment name:** `pypi`
1. Create a `pypi` environment in GitHub:
   Repo → **Settings** → **Environments** → **New environment** → name it `pypi`
   (Optional: enable **Required reviewers** for extra safety.)

### Releasing a new version

1. Bump version in `pyproject.toml`.

1. Commit and push:

   ```bash
   git add pyproject.toml
   git commit -m "Release v0.1.1"
   git tag v0.1.1
   git push origin main && git push origin v0.1.1
   ```

1. The workflow runs automatically and publishes to PyPI.

## 🤝 Contributing

Contributions are welcome. Please open an issue or pull request on the [GitHub repository](https://github.com/sahimco/sahim-django-common).

______________________________________________________________________

**SahimCo** — [GitHub](https://github.com/sahimco) · [PyPI](https://pypi.org/project/sahim-django-common/)

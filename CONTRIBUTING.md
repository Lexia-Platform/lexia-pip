# Contributing to Lexia Platform Integration Package

Thank you for your interest in contributing to the Lexia Platform Integration Package! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues
- Use the [GitHub Issues](https://github.com/Xalantico/lexia-pip/issues) page
- Provide a clear description of the problem
- Include steps to reproduce the issue
- Specify your environment (Python version, OS, etc.)

### Suggesting Features
- Open a new issue with the "enhancement" label
- Describe the feature and its benefits
- Provide use cases if possible

### Submitting Code Changes
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Ensure code follows the project's style guidelines
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 🧪 Development Setup

### Prerequisites
- Python 3.8 or higher
- pip
- git

### Local Development
```bash
# Clone the repository
git clone https://github.com/Xalantico/lexia-pip.git
cd lexia-pip

# Create virtual environment
python -m venv lexia_env
source lexia_env/bin/activate  # On Windows: lexia_env\Scripts\activate

# Install dependencies
pip install -r lexia/requirements.txt
pip install lexia[dev]

# Install package in editable mode
pip install -e .
```

### Using Make Commands
```bash
make help          # Show all available commands
make build         # Build the package
make test          # Test the package
make format        # Format code with black
make lint          # Run linting checks
```

## 📝 Code Style Guidelines

### Python Code
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Keep functions focused and single-purpose
- Add docstrings for public functions and classes

### Code Formatting
- Use Black for code formatting (line length: 88)
- Use isort for import sorting
- Run `make format` before committing

### Linting
- Use flake8 for linting
- Maximum line length: 88 characters
- Ignore E203 and W503 warnings

## 🧪 Testing

### Running Tests
```bash
# Basic import test
make test

# Full test suite (if tests directory exists)
make test-full

# Manual testing
python -c "import lexia; print('✅ Import successful')"
```

### Writing Tests
- Create tests in a `tests/` directory
- Use pytest as the testing framework
- Test both success and error cases
- Mock external dependencies when appropriate

## 📦 Building and Publishing

### Local Build
```bash
make build
```

### Publishing to Test PyPI
```bash
make publish-test
```

### Publishing to PyPI
```bash
make publish
```

## 📚 Documentation

### README Updates
- Keep the README.md up to date
- Update examples when APIs change
- Add new features to the documentation

### Code Comments
- Use clear, concise comments
- Explain complex logic
- Document any non-obvious design decisions

## 🚀 Release Process

1. Update version numbers in:
   - `pyproject.toml`
   - `setup.py`
   - `lexia/__init__.py`

2. Update CHANGELOG.md (if it exists)

3. Create a release tag:
   ```bash
   git tag v1.1.0
   git push origin v1.1.0
   ```

4. Build and publish:
   ```bash
   make publish
   ```

## 📞 Getting Help

- **Issues**: [GitHub Issues](https://github.com/Xalantico/lexia-pip/issues)
- **Email**: support@lexiaplatform.com
- **Discussions**: [GitHub Discussions](https://github.com/Xalantico/lexia-pip/discussions) (if enabled)

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You

Thank you for contributing to the Lexia Platform Integration Package! Your contributions help make this project better for everyone.

# 🚀 Lexia Platform Package - Installation & Usage Guide

## 📦 Package Successfully Created!

Your Lexia package has been converted into a professional pip package that can be easily installed and used by anyone.

## 🎯 Quick Installation

### For Users (Install from PyPI)
```bash
# Basic installation
pip install lexia

# With web dependencies (FastAPI, Uvicorn)
pip install lexia[web]

# For development
pip install lexia[dev]
```

### For Developers (Install from Source)
```bash
# Clone and install
git clone <your-repo-url>
cd lexia-platform
pip install -e .
```

## 🔧 What Was Created

### 1. **Package Configuration Files**
- `setup.py` - Traditional setup configuration
- `pyproject.toml` - Modern Python packaging standard
- `MANIFEST.in` - Controls which files are included
- `LICENSE` - MIT license for the package

### 2. **Build Tools**
- `build_package.py` - Python script for building/testing
- `Makefile` - Unix commands for package management
- `test_package.py` - Comprehensive test suite

### 3. **Package Structure**
```
lexia-platform/
├── lexia/                    # Main package
│   ├── __init__.py          # Package exports
│   ├── models.py            # Data models
│   ├── api_client.py        # HTTP client
│   ├── centrifugo_client.py # Real-time messaging
│   ├── unified_handler.py   # Main interface
│   ├── response_handler.py  # Response utilities
│   ├── utils.py             # Helper functions
│   └── web/                 # FastAPI integration
├── setup.py                  # Package configuration
├── pyproject.toml           # Modern packaging
├── MANIFEST.in              # File inclusion rules
├── LICENSE                  # MIT license
├── README.md                # Comprehensive documentation
├── build_package.py         # Build script
├── Makefile                 # Build commands
└── test_package.py          # Test suite
```

## 🚀 Usage Examples

### Basic Usage
```python
from lexia import LexiaHandler, ChatMessage

# Initialize
lexia = LexiaHandler()

# Use in your AI agent
async def process_message(data: ChatMessage):
    response = "Hello from your AI agent!"
    lexia.complete_response(data, response)
```

### FastAPI Integration
```python
from fastapi import FastAPI
from lexia import create_lexia_app, add_standard_endpoints

app = create_lexia_app(title="My AI Agent")
add_standard_endpoints(app, lexia_handler=lexia, process_message_func=your_ai_function)
```

## 🛠️ Development Commands

### Using Make (Recommended)
```bash
make help          # Show all commands
make build         # Build the package
make install       # Install locally
make test          # Test the package
make clean         # Clean build artifacts
make format        # Format code with black
make lint          # Run linting checks
```

### Using Python Scripts
```bash
python build_package.py help    # Show commands
python build_package.py build   # Build package
python build_package.py install # Install locally
python build_package.py test    # Test package
python build_package.py all     # Complete process
```

### Manual Commands
```bash
# Build
python -m build

# Install locally
pip install -e .

# Test
python test_package.py
```

## 📋 Publishing to PyPI

### 1. **Test PyPI (Recommended for testing)**
```bash
# Build package
make build

# Upload to Test PyPI
make publish-test
```

### 2. **Production PyPI**
```bash
# Build package
make build

# Upload to PyPI (requires credentials)
make publish
```

### 3. **Setup PyPI Credentials**
```bash
# Create ~/.pypirc file
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = your_username
password = your_password

[testpypi]
repository = https://test.pypi.org/legacy/
username = your_username
password = your_password
```

## 🧪 Testing

### Run Test Suite
```bash
python test_package.py
```

### Expected Output
```
🚀 Starting Lexia Platform Package Tests
==================================================

🔍 Running: Basic Imports
✅ Basic imports successful
✅ Basic Imports PASSED

🔍 Running: Version
📦 Package version: 1.1.0
✅ Version PASSED

🔍 Running: Data Models
✅ Variable model: TEST_VAR = test_value
✅ ChatMessage model: Hello, world!
✅ Data Models PASSED

🔍 Running: Response Handler
✅ Response created: success - Processing started
✅ Response Handler PASSED

🔍 Running: LexiaHandler
✅ LexiaHandler created successfully
✅ Method stream_chunk exists
✅ Method complete_response exists
✅ Method send_error exists
✅ LexiaHandler PASSED

🔍 Running: Web Imports
✅ Web imports successful
✅ Web Imports PASSED

==================================================
📊 Test Results: 6/6 tests passed
🎉 All tests passed! Package is working correctly.
```

## 🔄 Package Lifecycle

### 1. **Development**
```bash
# Make changes to your code
# Test locally
make test

# Build and install
make build
make install
```

### 2. **Testing**
```bash
# Test the package
python test_package.py

# Run linting
make lint

# Format code
make format
```

### 3. **Building**
```bash
# Clean previous builds
make clean

# Build package
make build

# Check what was created
ls -la dist/
```

### 4. **Publishing**
```bash
# Test PyPI first
make publish-test

# Production PyPI
make publish
```

## 📦 Package Features

### **Core Dependencies**
- `requests>=2.25.0` - HTTP client

- `pydantic>=2.0.0` - Data validation

### **Optional Dependencies**
- `fastapi>=0.100.0` - Web framework
- `uvicorn>=0.20.0` - ASGI server
- `pytest>=6.0` - Testing framework
- `black>=21.0` - Code formatting
- `flake8>=3.8` - Linting

### **Installation Options**
```bash
# Basic (core only)
pip install lexia

# With web framework
pip install lexia[web]

# With development tools
pip install lexia[dev]

# With everything
pip install lexia[web,dev]
```

## 🎉 Success!

Your Lexia package is now:

✅ **Professional** - Follows Python packaging standards  
✅ **Installable** - Can be installed with `pip install lexia`  
✅ **Testable** - Comprehensive test suite included  
✅ **Maintainable** - Clean build and development workflow  
✅ **Publishable** - Ready for PyPI distribution  
✅ **Documented** - Complete usage examples and guides  

## 🚀 Next Steps

1. **Test the package** - Run `python test_package.py`
2. **Build locally** - Use `make build` or `python build_package.py build`
3. **Install locally** - Use `make install` for development
4. **Publish to Test PyPI** - Test distribution with `make publish-test`
5. **Publish to PyPI** - Release to production with `make publish`

## 📞 Support

- **Documentation**: See `README.md` for comprehensive usage
- **Tests**: Run `python test_package.py` to verify functionality
- **Build Issues**: Use `make clean` then `make build`
- **Installation Issues**: Check dependencies with `pip list`

Your package is now ready for the world! 🌍

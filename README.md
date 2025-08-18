# Lexia Platform Integration Package

A clean, minimal Python package for seamless integration with the Lexia platform. This package provides essential components for AI agents to communicate with Lexia while maintaining platform-agnostic design.

## 🚀 Quick Start

### Install from PyPI (Recommended)
```bash
pip install lexia
```

### Install with web dependencies
```bash
pip install lexia[web]
```

### Install for development
```bash
pip install lexia[dev]
```

### Install from source
```bash
git clone https://github.com/Xalantico/lexia-pip.git
cd lexia-pip
pip install -e .
```

## 📦 Package Information

- **Package Name**: `lexia`
- **Version**: 1.1.0
- **Python**: >=3.8
- **License**: MIT
- **Dependencies**: requests, pydantic
- **Optional**: fastapi, uvicorn (web), pytest, black, flake8 (dev)

## 🎯 Purpose

This package provides a clean interface for AI agents to communicate with the Lexia platform. It handles all Lexia-specific communication while keeping your AI agent completely platform-agnostic.

## 🚀 Core Features

- **Real-time streaming** via Centrifugo
- **Backend communication** with Lexia
- **Response formatting** for Lexia compatibility
- **Data validation** with Pydantic models
- **Error handling** and notifications
- **FastAPI integration** with standard endpoints
- **Environment variable management**
- **API key handling**

## 📁 Package Structure

```
lexia/
├── __init__.py             # Clean exports only
├── models.py               # Lexia data models
├── response_handler.py     # Response creation utilities
├── unified_handler.py      # Single communication interface
├── api_client.py           # HTTP communication with Lexia backend
├── centrifugo_client.py    # Real-time updates via Centrifugo
├── utils.py                # Platform utilities
├── web/                    # FastAPI web framework utilities
│   ├── __init__.py
│   ├── app_factory.py
│   └── endpoints.py
└── requirements.txt        # Package dependencies
```

## 🚀 Usage Examples

### Basic Usage
```python
from lexia import LexiaHandler, ChatMessage

# Initialize the handler
lexia = LexiaHandler()

# Use in your AI agent
async def process_message(data: ChatMessage):
    # Your AI logic here...
    response = "Hello from your AI agent!"
    lexia.complete_response(data, response)
```

### FastAPI Integration
```python
from fastapi import FastAPI
from lexia import create_lexia_app, add_standard_endpoints, LexiaHandler

# Create FastAPI app
app = create_lexia_app(title="My AI Agent")

# Initialize Lexia handler
lexia = LexiaHandler()

# Add standard endpoints
add_standard_endpoints(
    app, 
    lexia_handler=lexia,
    process_message_func=your_ai_function
)
```

## 🔧 Core Components

### LexiaHandler (Main Interface)
Single, clean interface for all Lexia communication:

```python
from lexia import LexiaHandler

lexia = LexiaHandler()

# Stream AI response chunks
lexia.stream_chunk(data, content)

# Complete AI response
lexia.complete_response(data, full_response)

# Send error messages
lexia.send_error(data, error_message)
```

### Data Models
Lexia's expected data formats:

```python
from lexia import ChatMessage, ChatResponse, Variable

# ChatMessage - Lexia's request format
# ChatResponse - Lexia's expected response format  
# Variable - Environment variables from Lexia
```

### Response Handler
Create Lexia-compatible responses:

```python
from lexia import create_success_response

response = create_success_response(
    response_uuid="uuid123",
    thread_id="thread456"
)
```

## 💡 Complete Example: AI Agent with FastAPI

```python
import asyncio
from fastapi import FastAPI
from lexia import (
    LexiaHandler, 
    ChatMessage, 
    create_lexia_app,
    add_standard_endpoints
)

# Initialize services
lexia = LexiaHandler()

# Create FastAPI app
app = create_lexia_app(
    title="My AI Agent",
    version="1.1.0",
    description="Custom AI agent with Lexia integration"
)

# Define your AI logic
async def process_message(data: ChatMessage):
    """Your custom AI processing logic goes here."""
    try:
        # Example: Simple echo response
        response = f"AI Agent processed: {data.message}"
        
        # Stream response chunks (optional)
        for word in response.split():
            lexia.stream_chunk(data, word + " ")
            await asyncio.sleep(0.1)
        
        # Complete the response
        lexia.complete_response(data, response)
        
    except Exception as e:
        lexia.send_error(data, str(e))

# Add all standard Lexia endpoints
add_standard_endpoints(
    app, 
    conversation_manager=None,
    lexia_handler=lexia,
    process_message_func=process_message
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## 🔄 Integration Flow

```
Your AI Agent → LexiaHandler → Lexia Platform
     ↓              ↓              ↓
  OpenAI/LLM   Communication   Real-time + Backend
```

Your AI agent focuses on AI logic, this package handles all Lexia communication complexity behind a clean interface.

## 📋 Development Setup

### Using Make (Recommended)
```bash
# Show available commands
make help

# Setup development environment
make dev
source lexia_env/bin/activate
make deps

# Build and test
make build
make test
make install
```

### Manual Setup
```bash
# Create virtual environment
python3 -m venv lexia_env
source lexia_env/bin/activate

# Install dependencies
pip install -r lexia/requirements.txt
pip install build twine

# Build package
python -m build

# Install locally
pip install -e .
```

## 🧪 Testing

```python
import pytest
from lexia import LexiaHandler, ChatMessage

def test_lexia_handler():
    """Test basic LexiaHandler functionality."""
    handler = LexiaHandler()
    
    # Create test data
    test_data = ChatMessage(
        thread_id="test123",
        model="gpt-4",
        message="Hello",
        conversation_id=1,
        response_uuid="uuid123",
        message_uuid="msg123",
        channel="test",
        file_type="",
        file_url="",
        variables=[],
        url="http://test.com",
        url_update="",
        url_upload="",
        force_search=False,
        system_message=None,
        memory=[],
        project_system_message=None,
        first_message=False,
        project_id="",
        project_files=None
    )
    
    # Test that handler can be created
    assert handler is not None
    assert hasattr(handler, 'stream_chunk')
    assert hasattr(handler, 'complete_response')
    assert hasattr(handler, 'send_error')

if __name__ == "__main__":
    pytest.main([__file__])
```

## 🚨 Common Issues and Solutions

### Import Error
```bash
ModuleNotFoundError: No module named 'lexia'
```
**Solution**: Ensure you're in the correct directory or add the lexia folder to your Python path.

### Missing Dependencies
```bash
ImportError: No module named 'fastapi'
```
**Solution**: Install requirements: `pip install -r lexia/requirements.txt` or use `pip install lexia[web]`

### Lexia Communication Fails
**Solution**: Verify that your environment variables and API keys are properly configured in the Lexia request variables.

## 📦 Publishing

### Test PyPI
```bash
make build
make publish-test
```

### Production PyPI
```bash
make build
make publish
```

## 🎯 Design Principles

1. **Single Responsibility**: Each component has one clear purpose
2. **Clean Interface**: Simple, intuitive methods
3. **Platform Agnostic**: Your AI agent doesn't know about Lexia internals
4. **Minimal Dependencies**: Only what's absolutely necessary
5. **Easy Testing**: Simple, focused components

## 🚀 Benefits

- **Clean separation** between your AI agent and Lexia
- **Easy to maintain** - all Lexia logic in one place
- **Easy to replace** - switch platforms by replacing this package
- **Professional structure** - clean, organized code
- **Fast development** - no complex integrations to manage
- **Drop-in replacement** - copy folder and start using immediately

## 📞 Support

This package is designed to be a drop-in solution - just `pip install lexia` and start building your AI agent! All Lexia communication is handled automatically, standard endpoints are provided out-of-the-box, and your AI agent remains completely platform-agnostic.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📚 Documentation

For more detailed documentation, please refer to the inline code comments and examples provided in this README.

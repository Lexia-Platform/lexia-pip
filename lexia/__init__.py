"""
Lexia Integration Package
========================

Clean, minimal package for Lexia platform integration.
Contains only essential components for communication.
"""

__version__ = "1.1.0"

from .models import ChatResponse, ChatMessage, Variable
from .response_handler import create_success_response
from .unified_handler import LexiaHandler
from .utils import get_variable_value, get_openai_api_key

# Web framework utilities
try:
    from .web import create_lexia_app, add_standard_endpoints
    __all__ = [
        'ChatResponse', 'ChatMessage', 'Variable',
        'create_success_response', 'LexiaHandler',
        'get_variable_value', 'get_openai_api_key',
        'create_lexia_app', 'add_standard_endpoints',
        '__version__'
    ]
except ImportError:
    # Fallback if web dependencies aren't available
    __all__ = [
        'ChatResponse', 'ChatMessage', 'Variable',
        'create_success_response', 'LexiaHandler',
        'get_variable_value', 'get_openai_api_key',
        '__version__'
    ]

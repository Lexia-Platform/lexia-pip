# Changelog

All notable changes to the Lexia Platform Integration Package will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.8] - 2025-11-02

### Added
- Added `sleep_time` parameter to `ChatMessage` model for configurable timing control
- Added `force_tools` parameter to `ChatMessage` model (list of tool names like ['code', 'search', 'xyz'])
- Added `ForceToolsHelper` class for easy access to forced tools with methods like `has()`, `has_code()`, `has_search()`, `get_all()`, etc.

### Removed
- Removed deprecated `force_search` boolean parameter (replaced by `force_tools`)
- Removed deprecated `force_code` boolean parameter (replaced by `force_tools`)

### Changed
- Tool forcing now uses a flexible list-based approach instead of individual boolean flags

## [1.2.6] - 2025-01-14

### Added
- Error logging to Lexia backend via `/api/internal/v1/logs` endpoint
- Enhanced `send_error()` method with optional `trace` and `exception` parameters for detailed error logging
- Automatic extraction and truncation of stack traces for error logs
- Support for error level, location tracking, and additional metadata in error logs

### Fixed
- Fixed Centrifugo client to send actual error message instead of hardcoded text
- Fixed dev mode error streaming to match normal response flow (delta + complete)
- Improved error message visibility in both dev and production modes

## [1.1.0] - 2025-08-18

### Added
- Initial release of Lexia Platform Integration Package
- `LexiaHandler` class for unified communication interface
- Data models for Lexia platform compatibility
- Response handling utilities
- FastAPI integration with standard endpoints
- Real-time streaming support
- Environment variable management
- API key handling utilities

### Features
- Clean, minimal package design
- Platform-agnostic AI agent integration
- Comprehensive error handling
- Easy-to-use API for developers
- Professional package structure
- MIT license for open source use

### Documentation
- Comprehensive README with examples
- Installation and usage instructions
- Development setup guide
- Contributing guidelines
- GitHub Actions CI workflow



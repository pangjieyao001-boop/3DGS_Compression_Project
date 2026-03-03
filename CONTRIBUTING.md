# Contributing to 3DGS Compression Project

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version, PyTorch version)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:
- Clear description of the proposed feature
- Rationale and use cases
- Potential implementation approach (if applicable)

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add docstrings for functions and classes
- Keep functions focused and modular
- Comment complex algorithms

### Testing

Before submitting:
- Test your changes locally
- Ensure existing functionality still works
- Add tests for new features

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/3DGS_Compression_Project.git
cd 3DGS_Compression_Project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
pip install -r requirements-dev.txt
```

## Questions?

Feel free to open an issue for questions or join discussions.

Thank you for contributing!

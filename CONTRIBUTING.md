# Contributing to HTMLx

Thank you for your interest in contributing to HTMLx! Here's how you can help:

## Getting Started

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/Aquib489/htmlx.git`
3. **Create a branch**: `git checkout -b feature/your-feature-name`
4. **Make changes** and commit: `git commit -am "Add your feature"`
5. **Push**: `git push origin feature/your-feature-name`
6. **Create a Pull Request**

## Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/unit/test_parser.py -v

# Test compilation
python cli.py example.htmlx test_output/ --verbose
```

## Code Guidelines

- Follow PEP 8 style guide
- Write tests for new features
- Update documentation when needed
- Keep commits focused and descriptive

## Adding Tests

1. Add test functions to `tests/unit/test_parser.py`
2. Test format: `def test_feature_name():`
3. Run tests: `pytest tests/unit/test_parser.py::test_feature_name -v`

## Reporting Issues

Use the GitHub Issues tab to report:
- Bugs
- Feature requests
- Documentation improvements
- Questions

Include:
- Clear description of the issue
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Your environment (Python version, OS, etc.)

## Pull Request Process

1. Update documentation if needed
2. Add tests for new features
3. Ensure all tests pass: `pytest tests/unit/test_parser.py -v`
4. Keep pull requests focused on a single feature
5. Write clear commit messages

## Areas for Contribution

- **Parser improvements**: Better error messages, performance optimizations
- **Generators**: New features for HTML/CSS/JS output
- **Documentation**: Examples, tutorials, API docs
- **Examples**: Real-world use cases
- **Testing**: More test coverage
- **Tools**: IDE extensions, linters, formatters

## Questions?

Feel free to:
- Open an issue for discussion
- Check existing issues and documentation
- Review the code comments

Thank you for making HTMLx better! 🚀


# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project that demonstrates how to use the Anthropic Claude API. The codebase contains a simple example script showing Claude API usage with Japanese language support.

## Project Structure

- `claude_api.py` - Main example script with Japanese documentation showing Claude API usage

## Development Setup

### Dependencies
Install required Python packages:
```bash
pip install anthropic python-dotenv
```

### Environment Configuration
Set up your Anthropic API key as an environment variable:
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Or create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your-api-key-here
```

## Code Architecture

The project demonstrates direct Claude API usage with:
- Environment variable loading using python-dotenv
- Error handling for API calls
- Japanese language prompts and responses
- Poetry-focused system prompt

## Running the Example

Execute the main example:
```bash
python claude_api.py
```

## Testing

Run the test suite:
```bash
python -m unittest test_claude_api.py
```

Or run with verbose output:
```bash
python -m unittest test_claude_api.py -v
```

The test suite includes:
- API key validation tests
- Successful API call simulation
- Parameter validation
- Error handling verification
- Environment variable loading tests

## API Models

The example uses the latest Claude model:
- `claude-opus-4-20250514`
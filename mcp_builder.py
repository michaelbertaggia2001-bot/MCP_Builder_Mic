#!/usr/bin/env python3
"""
MCP Builder Snello - Generatore server MCP

Genera server MCP (Model Context Protocol) di alta qualità con best practices integrate.
"""

import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum
import json
import subprocess
import sys
from pydantic import BaseModel, Field, ConfigDict
from mcp.server.fastmcp import FastMCP

class Language(Enum):
    PYTHON = "python"
    TYPESCRIPT = "typescript"

class Transport(Enum):
    STDIO = "stdio"
    SSE = "sse"
    HTTP = "http"

@dataclass
class MCPConfig:
    service_name: str
    language: Language
    transport: Transport
    generate_evaluation: bool

class MCPBuilder:
    def __init__(self):
        self.project_dir = Path.cwd()
    
    def generate_server(self, config: MCPConfig):
        """Genera un server MCP completo."""
        print(f"[INFO] Generating {config.language.value} MCP server for: {config.service_name}")
        
        if config.language == Language.PYTHON:
            self._generate_python_server(config)
        elif config.language == Language.TYPESCRIPT:
            self._generate_typescript_server(config)
    
    def _generate_python_server(self, config: MCPConfig):
        """Genera server Python usando FastMCP."""
        service_dir = self.project_dir / f"{config.service_name.replace('-', '_')}_mcp"
        service_dir.mkdir(exist_ok=True)
        
        # Genera file principale
        self._write_python_server(config, service_dir)
        
        # Genera file di test
        self._write_python_test(config, service_dir)
        
        # Genera requirements.txt
        self._write_python_requirements(config, service_dir)
        
        # Genera pyproject.toml
        self._write_pyproject_toml(config, service_dir)
        
        # Genera README.md
        self._write_readme(config, service_dir)
        
        # Genera .gitignore
        self._write_gitignore(config, service_dir)
        
        # Genera LICENSE
        self._write_license(config, service_dir)
        
        # Genera CHANGELOG.md
        self._write_changelog(config, service_dir)
        
        # Crea ambiente virtuale .venv
        self._create_venv(config, service_dir)
        
        # Genera evaluation se richiesto
        if config.generate_evaluation:
            self._write_evaluation(config, service_dir)
        
        print(f"[OK] MCP server generated in: {service_dir}")
        print(f"[VENV] Virtual environment created in: {service_dir}/.venv")
        print(f"[TEST] To test: cd {service_dir.name}")
        print(f"[TEST] Then: .venv\\Scripts\\python test_server.py")
    
    def _write_python_server(self, config: MCPConfig, service_dir: Path):
        """Scrive il file principale del server Python."""
        content = f'''#!/usr/bin/env python3
"""
{config.service_name.title()} MCP Server

Generated with MCP Builder Snello following Claude's best practices.
"""

import asyncio
import json
import httpx
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("{config.service_name}_mcp")

# Constants
API_BASE_URL = "https://api.{config.service_name}.com/v1"
CHARACTER_LIMIT = 25000  # Maximum response size in characters

# Pydantic Models for Input Validation
class {config.service_name.replace('-', '').title()}ListResourcesInput(BaseModel):
    """Input model for {config.service_name}-list_resources operation."""
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        extra='forbid'
    )

    limit: int = Field(default=20, description="Number of results")
    offset: int = Field(default=0, description="Skip results")

class {config.service_name.replace('-', '').title()}GetResourceInput(BaseModel):
    """Input model for {config.service_name}-get_resource operation."""
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        extra='forbid'
    )

    resource_id: str = Field(description="Resource ID", min_length=1)

# Shared utility functions
async def _make_api_request(endpoint: str, method: str = "GET", **kwargs) -> dict:
    """Reusable function for all API calls."""
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method,
            f"{{API_BASE_URL}}/{{endpoint}}",
            timeout=30.0,
            **kwargs
        )
        response.raise_for_status()
        return response.json()

def _handle_api_error(e: Exception) -> str:
    """Consistent error formatting across all tools."""
    if isinstance(e, httpx.HTTPStatusError):
        if e.response.status_code == 404:
            return "Error: Resource not found. Please check the ID is correct."
        elif e.response.status_code == 403:
            return "Error: Permission denied. You don't have access to this resource."
        elif e.response.status_code == 429:
            return "Error: Rate limit exceeded. Please wait before making more requests."
        return f"Error: API request failed with status {{e.response.status_code}}"
    elif isinstance(e, httpx.TimeoutException):
        return "Error: Request timed out. Please try again."
    elif isinstance(e, httpx.ConnectError):
        return "Error: Connection failed. Please check your internet connection."
    return f"Error: Unexpected error occurred: {{type(e).__name__}}: {{str(e)}}"

# Tool definitions
@mcp.tool(
    name="{config.service_name}-list_resources",
    annotations={{'title': '{config.service_name.title()} List Resources', 'readOnlyHint': True, 'destructiveHint': False, 'idempotentHint': True, 'openWorldHint': True}}
)
async def {config.service_name.replace('-', '_')}_list_resources(params: {config.service_name.replace('-', '').title()}ListResourcesInput) -> str:
    """List resources from {config.service_name}
    
    Args:
        params ({config.service_name.replace('-', '').title()}ListResourcesInput): Validated input parameters

    Returns:
        str: JSON-formatted response containing operation results
    """
    try:
        # TODO: Implement {config.service_name}-list_resources logic
        # Example API call structure:
        # data = await _make_api_request("resources", params=params.model_dump())
        # return json.dumps(data, indent=2)
        
        return json.dumps({{"status": "success", "message": "{config.service_name}-list_resources implemented"}})
        
    except Exception as e:
        return _handle_api_error(e)

@mcp.tool(
    name="{config.service_name}-get_resource",
    annotations={{'title': '{config.service_name.title()} Get Resource', 'readOnlyHint': True, 'destructiveHint': False, 'idempotentHint': True, 'openWorldHint': True}}
)
async def {config.service_name.replace('-', '_')}_get_resource(params: {config.service_name.replace('-', '').title()}GetResourceInput) -> str:
    """Get a specific resource from {config.service_name}
    
    Args:
        params ({config.service_name.replace('-', '').title()}GetResourceInput): Validated input parameters

    Returns:
        str: JSON-formatted response containing operation results
    """
    try:
        # TODO: Implement {config.service_name}-get_resource logic
        # Example API call structure:
        # data = await _make_api_request("resources/{{resource_id}}", params=params.model_dump())
        # return json.dumps(data, indent=2)
        
        return json.dumps({{"status": "success", "message": "{config.service_name}-get_resource implemented"}})
        
    except Exception as e:
        return _handle_api_error(e)

if __name__ == "__main__":
    mcp.run(transport="{config.transport.value}")
'''
        
        with open(service_dir / f"{config.service_name.replace('-', '_')}_mcp.py", "w") as f:
            f.write(content)
    
    def _write_python_test(self, config: MCPConfig, service_dir: Path):
        """Scrive il file di test Python."""
        content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test file for {config.service_name} MCP Server

Run this to test your generated MCP server:
    python test_server.py
"""

import asyncio
import subprocess
import sys
from pathlib import Path

def test_server():
    """Test the generated MCP server."""
    import os
    original_cwd = os.getcwd()
    
    # Se siamo già nella directory del server, non serve cambiare directory
    server_file = Path(f"{config.service_name.replace('-', '_')}_mcp.py")
    if not server_file.exists():
        print(f"[ERROR] Server file {config.service_name.replace('-', '_')}_mcp.py not found in current directory!")
        return False
    
    print(f"[TEST] Testing {config.service_name.replace('-', '_')}_mcp.py...")
    
    # Test basic import
    try:
        import {config.service_name.replace('-', '_')}_mcp
        print("[OK] Server imports successfully")
    except Exception as e:
        print(f"[ERROR] Import failed: {{e}}")
        return False

    # Test FastMCP initialization
    try:
        mcp = {config.service_name.replace('-', '_')}_mcp.mcp
        print(f"[OK] FastMCP server initialized: {{mcp.name}}")
    except Exception as e:
        print(f"[ERROR] FastMCP initialization failed: {{e}}")
        return False

    # Test che le funzioni tool principali esistano
    try:
        # Import del modulo principale  
        import {config.service_name.replace('-', '_')}_mcp as mcp_module
        
        # Test che le funzioni tool principali esistano
        expected_functions = ['{config.service_name.replace('-', '_')}_list_resources', '{config.service_name.replace('-', '_')}_get_resource']
        found_functions = []
        
        for func_name in expected_functions:
            if hasattr(mcp_module, func_name):
                func = getattr(mcp_module, func_name)
                if callable(func):
                    found_functions.append(func_name)
                    print('  [OK] ' + func_name + ' function found and is callable')
                else:
                    print('  [FAIL] ' + func_name + ' exists but is not callable')
                    return False
            else:
                print('  [FAIL] Missing function: ' + func_name)
                return False
        
        print('[OK] Found ' + str(len(found_functions)) + ' tool functions: ' + str(found_functions))
    except Exception as e:
        print('[ERROR] Tool discovery failed: ' + str(e))
        return False
        
    print("[OK] All basic tests passed!")
    return True

if __name__ == "__main__":
    success = test_server()
    sys.exit(0 if success else 1)
'''
        
        with open(service_dir / "test_server.py", "w") as f:
            f.write(content)
    
    def _write_python_requirements(self, config: MCPConfig, service_dir: Path):
        """Scrive requirements.txt per Python."""
        content = '''mcp[cli]
httpx>=0.28.0
pydantic>=2.0.0
python-dotenv>=1.0.0
'''
        
        with open(service_dir / "requirements.txt", "w") as f:
            f.write(content)
    
    def _create_venv(self, config: MCPConfig, service_dir: Path):
        """Crea ambiente virtuale .venv nella directory del progetto."""
        venv_dir = service_dir / ".venv"
        if venv_dir.exists():
            print(f"[INFO] Virtual environment already exists at {venv_dir}")
            return
        
        try:
            print(f"[INFO] Creating virtual environment at {venv_dir}...")
            subprocess.run(
                [sys.executable, "-m", "venv", str(venv_dir)],
                check=True,
                capture_output=True
            )
            print(f"[OK] Virtual environment created successfully")
        except subprocess.CalledProcessError as e:
            print(f"[WARNING] Failed to create virtual environment: {e}")
            print(f"[INFO] You can create it manually with: python -m venv .venv")
    
    def _write_pyproject_toml(self, config: MCPConfig, service_dir: Path):
        """Scrive pyproject.toml per packaging moderno Python."""
        service_name_clean = config.service_name.replace('-', '_')
        service_name_title = config.service_name.replace('-', ' ').title()
        
        content = f'''[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{service_name_clean}-mcp"
version = "0.1.0"
description = "{service_name_title} MCP Server - Model Context Protocol server"
readme = "README.md"
requires-python = ">=3.10"
license = {{text = "MIT"}}
authors = [
    {{name = "Your Name", email = "your.email@example.com"}},
]
keywords = ["mcp", "model-context-protocol", "fastmcp", "{config.service_name}"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

dependencies = [
    "mcp[cli]>=1.0.0",
    "httpx>=0.28.0",
    "pydantic>=2.0.0",
    "python-dotenv>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
]

[project.scripts]
{service_name_clean}-mcp = "{service_name_clean}_mcp:main"

[tool.setuptools.packages.find]
where = ["."]
include = ["{service_name_clean}_mcp*"]

[tool.black]
line-length = 100
target-version = ['py310']

[tool.ruff]
line-length = 100
target-version = "py310"
'''
        
        with open(service_dir / "pyproject.toml", "w", encoding="utf-8") as f:
            f.write(content)
    
    def _write_readme(self, config: MCPConfig, service_dir: Path):
        """Scrive README.md completo e GitHub-ready."""
        service_name_clean = config.service_name.replace('-', '_')
        service_name_title = config.service_name.replace('-', ' ').title()
        
        content = f'''# {service_name_title} MCP Server

Model Context Protocol (MCP) server for {config.service_name}, built with FastMCP framework.

## Overview

This MCP server provides tools and resources for interacting with {config.service_name} through the Model Context Protocol, enabling AI assistants like Claude to access {config.service_name} functionality.

## Features

- FastMCP framework for high-performance MCP servers
- Async HTTP client with httpx
- Input validation with Pydantic v2
- Comprehensive error handling
- Type-safe API with Python type hints

## Requirements

- Python >=3.10
- Virtual environment (`.venv` created automatically)

## Installation

1. Clone or navigate to this directory:
```bash
cd {service_name_clean}_mcp
```

2. Activate the virtual environment:

**Windows (PowerShell):**
```powershell
.venv\\Scripts\\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\\Scripts\\activate.bat
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install as a package:
```bash
pip install -e .
```

## Usage

### Run the Server

```bash
python {service_name_clean}_mcp.py
```

### Test the Server

```bash
python test_server.py
```

### MCP Client Configuration

Add to your MCP client configuration (e.g., Claude Desktop):

```json
{{
  "mcpServers": {{
    "{config.service_name}": {{
      "command": ".venv\\\\Scripts\\\\python",
      "args": ["{service_name_clean}_mcp.py"],
      "env": {{
        "API_KEY": "your-api-key-here"
      }}
    }}
  }}
}}
```

**Note:** For Windows PowerShell, use double backslashes `\\\\` in paths.

## Tools

### {config.service_name}-list_resources

List resources from {config.service_name}.

**Parameters:**
- `limit` (int, default: 20): Number of results
- `offset` (int, default: 0): Skip results

### {config.service_name}-get_resource

Get a specific resource from {config.service_name}.

**Parameters:**
- `resource_id` (str): Resource identifier

## Development

### Setup Development Environment

```bash
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

### Code Formatting

```bash
black .
ruff check .
```

## Project Structure

```
{service_name_clean}_mcp/
├── {service_name_clean}_mcp.py      # Main server file
├── test_server.py                   # Test suite
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Modern Python packaging
├── README.md                        # This file
├── CHANGELOG.md                     # Project changelog
├── LICENSE                          # MIT License
├── .gitignore                      # Git ignore patterns
└── .venv/                          # Virtual environment (not in git)
```

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Support

For issues and questions, please open an issue on GitHub.

---

**Generated with MCP Builder** - FastMCP best practices included.
'''
        
        with open(service_dir / "README.md", "w", encoding="utf-8") as f:
            f.write(content)
    
    def _write_gitignore(self, config: MCPConfig, service_dir: Path):
        """Scrive .gitignore appropriato per progetto Python."""
        content = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
.venv/
venv/
ENV/
env/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
.hypothesis/

# Environment variables
.env
.env.local
.env.*.local

# MCP specific
*.log
evaluation.xml

# OS
Thumbs.db
'''
        
        with open(service_dir / ".gitignore", "w", encoding="utf-8") as f:
            f.write(content)
    
    def _write_license(self, config: MCPConfig, service_dir: Path):
        """Scrive LICENSE template MIT."""
        from datetime import datetime
        year = datetime.now().year
        
        content = f'''MIT License

Copyright (c) {year} {service_dir.name} contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
        
        with open(service_dir / "LICENSE", "w", encoding="utf-8") as f:
            f.write(content)
    
    def _write_changelog(self, config: MCPConfig, service_dir: Path):
        """Scrive CHANGELOG.md template."""
        from datetime import datetime
        date = datetime.now().strftime("%Y-%m-%d")
        service_name_title = config.service_name.replace('-', ' ').title()
        
        content = f'''# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup
- {service_name_title} MCP Server implementation
- Basic tools: list_resources and get_resource
- FastMCP framework integration
- Pydantic v2 input validation
- Comprehensive error handling
- Test suite

## [0.1.0] - {date}

### Added
- Initial release
- Generated with MCP Builder

[Unreleased]: https://github.com/your-username/{config.service_name.replace('-', '_')}-mcp/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/your-username/{config.service_name.replace('-', '_')}-mcp/releases/tag/v0.1.0
'''
        
        with open(service_dir / "CHANGELOG.md", "w", encoding="utf-8") as f:
            f.write(content)
    
    def _write_evaluation(self, config: MCPConfig, service_dir: Path):
        """Scrive evaluation.xml."""
        content = f'''<?xml version="1.0" encoding="UTF-8"?>
<evaluation>
    <qa_pair>
        <question>Use the {config.service_name}-list_resources tool to demonstrate its functionality</question>
        <answer>Tool {config.service_name}-list_resources executed successfully</answer>
    </qa_pair>
    <qa_pair>
        <question>Use the {config.service_name}-get_resource tool to retrieve a specific resource</question>
        <answer>Tool {config.service_name}-get_resource executed successfully</answer>
    </qa_pair>
</evaluation>
'''
        
        with open(service_dir / "evaluation.xml", "w", encoding="utf-8") as f:
            f.write(content)
    
    def _generate_typescript_server(self, config: MCPConfig):
        """Genera server TypeScript usando McpServer."""
        # TODO: Implement TypeScript generation
        print("[ERROR] TypeScript generation not yet implemented")
        return

def main():
    parser = argparse.ArgumentParser(description="MCP Builder Snello - Generate MCP servers")
    parser.add_argument("--service", required=True, help="Service name (e.g., github, slack)")
    parser.add_argument("--python", action="store_true", help="Generate Python server")
    parser.add_argument("--typescript", action="store_true", help="Generate TypeScript server")
    parser.add_argument("--transport", choices=["stdio", "sse", "http"], default="stdio", help="Transport type")
    parser.add_argument("--no-evaluation", action="store_true", help="Skip evaluation generation")
    
    args = parser.parse_args()
    
    if not args.python and not args.typescript:
        print("Error: Specify either --python or --typescript")
        return
    
    language = Language.PYTHON if args.python else Language.TYPESCRIPT
    transport = Transport(args.transport)
    
    config = MCPConfig(
        service_name=args.service,
        language=language,
        transport=transport,
        generate_evaluation=not args.no_evaluation
    )
    
    builder = MCPBuilder()
    builder.generate_server(config)
    
    print(f"[SUCCESS] MCP server generated successfully!")
    print(f"[INFO] Next steps:")
    print(f"1. cd {config.service_name.replace('-', '_')}_mcp")
    print(f"2. Activate virtual environment:")
    print(f"   .venv\\Scripts\\Activate.ps1  (PowerShell)")
    print(f"   .venv\\Scripts\\activate.bat  (CMD)")
    print(f"3. Install dependencies:")
    print(f"   pip install -r requirements.txt")
    print(f"4. Implement your API logic in the generated server")
    print(f"5. Test with: .venv\\Scripts\\python test_server.py")

if __name__ == "__main__":
    main()

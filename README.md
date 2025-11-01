# MCP Builder - Model Context Protocol Builder

## Project Overview

Questo repository contiene MCP Builder, uno strumento professionale per la generazione automatica di server MCP (Model Context Protocol). Il progetto fornisce template di alta qualità e best practices per lo sviluppo di integrazioni MCP.

## Project Structure

```
MCP Builder/
├── mcp_builder.py          # Tool principale per creare MCP server
├── requirements.txt        # Dipendenze Python
├── LICENSE                 # Licenza MIT open source
├── .gitignore              # File di configurazione Git
└── README.md              # Questo file
```

## Features

### MCP Builder Core
- Generazione automatica di server MCP professionali
- Template Python con FastMCP framework
- Input validation avanzata con Pydantic v2
- Error handling robusto e logging completo
- Supporto per trasporti stdio, HTTP e SSE
- Ambiente virtuale integrato (.venv)
- Test suite automatica inclusa

### Generated Server Features
- FastMCP framework per performance elevate
- Async HTTP client con httpx
- Type-safe API con Python type hints
- Comprehensive error handling
- Professional logging
- GitHub-ready project structure

## Quick Start

### 1. Installazione

```bash
# Clona o scarica il repository
git clone https://github.com/MIC-username/MCP_Builder_MIC.git
cd MCP_Builder_MIC

# Installa dipendenze
pip install -r requirements.txt
```

### 2. Genera un Nuovo MCP Server

```bash
python mcp_builder.py --service your-service --python --transport stdio
```

### 3. Test del Server Generato

```bash
cd your_service_mcp
.venv\Scripts\Activate.ps1  # PowerShell Windows
# .venv/bin/activate       # macOS/Linux
pip install -r requirements.txt
.venv\Scripts\python test_server.py
```

## Example Usage

### Generare Server GitHub

```bash
python mcp_builder.py --service github --python --transport stdio
```

### Generare Server Weather API

```bash
python mcp_builder.py --service weather-api --python --transport http
```

### Generare Server con TypeScript

```bash
python mcp_builder.py --service my-service --typescript --transport sse
```

## Generated Project Structure

Ogni server generato include:

```
your_service_mcp/
├── your_service_mcp.py      # Main server file
├── test_server.py           # Automated tests
├── requirements.txt         # Python dependencies
├── pyproject.toml          # Modern Python packaging
├── README.md               # Service documentation
├── CHANGELOG.md            # Version tracking
├── LICENSE                 # MIT License
├── .gitignore             # Git configuration
├── .venv/                 # Virtual environment
└── evaluation.xml         # MCP evaluation tests
```

## Requirements

- Python 3.8+
- FastMCP framework
- httpx for async HTTP
- pydantic for validation
- Virtual environment support

## Architecture

### Core Components

1. **MCPBuilder Class**: Generazione automatica server
2. **Template System**: Template Python/TypeScript ottimizzati
3. **Validation Layer**: Pydantic v2 input validation
4. **Error Handling**: Comprehensive error management
5. **Test Suite**: Automated testing framework

### Design Principles

- **Production Ready**: Enterprise-grade code quality
- **Security First**: Safe credential handling
- **Performance Optimized**: Async/await patterns
- **Developer Friendly**: Clear documentation and examples
- **Standards Compliant**: MCP protocol specifications

## Best Practices

### Generated Code Features
- Input validation with Pydantic models
- Async HTTP client with proper error handling
- Type hints throughout
- Comprehensive logging
- Environment-based configuration
- Secure API key management

### Windows PowerShell Compatibility
- Tested with PowerShell 5 and 7+
- UTF-8 encoding support
- No emoji or special characters
- Cross-platform compatibility

## Success Metrics

### Code Quality
- 100% Success Rate per template generation
- Production-ready generated servers
- Comprehensive test coverage
- Professional error handling

### Developer Experience
- One-command server generation
- Automated virtual environment setup
- GitHub-ready project structure
- Clear documentation and examples

## Use Cases

### API Integrations
- REST API wrappers
- Database connectors
- External service integrations
- Custom business logic servers

### Development Tools
- Code generation templates
- Development automation
- Testing frameworks
- Documentation generators

## Next Steps

1. **Generate Your Server**: `python mcp_builder.py --service your-api`
2. **Customize Logic**: Implement your API calls in the generated server
3. **Test Thoroughly**: Run the automated test suite
4. **Deploy**: Connect to your MCP client (Claude Desktop, etc.)
5. **Contribute**: Share your templates with the community

## Support & Community

- **GitHub Issues**: Bug reports and feature requests
- **Documentation**: Comprehensive guides and examples
- **Contributions**: Welcome! Please read our contributing guidelines
- **Examples**: Explore generated examples in the repository

## License

MIT License - see LICENSE file for full details.

## About

MCP Builder MIC is dedicated to advancing MCP (Model Context Protocol) adoption by providing high-quality, production-ready server generation tools.

**Project Founder**: MIC  
**Version**: 1.0.0  
**Status**: Production Ready  

---

*Generated with MCP Builder - Professional MCP Server Generation Tool*
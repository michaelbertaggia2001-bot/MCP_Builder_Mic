   ![Python](https://img.shields.io/badge/python-3.8+-blue)
   ![License](https://img.shields.io/badge/license-MIT-green)
   ![Status](https://img.shields.io/badge/status-production--ready-success)

# MCP Builder - Model Context Protocol Builder

## About

💡 MCP Builder: La piattaforma definitiva per sviluppatori vibe coder. Template premium, testing automatizzato, best practices integrate. Da concept a produzione in pochi minuti

## Project Overview

Tool professionale per generare automaticamente server MCP (Model Context Protocol) production-ready. Template Python/TypeScript, FastMCP framework, validazione Pydantic v2, test suite automatica

## Quick Start

### 1. Installazione

```bash
git clone https://github.com/michaelbertaggia2001-bot/MCP_Builder_Mic.git
cd MCP_Builder_Mic
pip install -r requirements.txt
```

### 2. Genera Server MCP

```bash
python mcp_builder.py --service your-service --python --transport stdio
```

### 3. Test e Configurazione

```bash
cd your_service_mcp
.venv\Scripts\Activate.ps1  # PowerShell
pip install -r requirements.txt
.venv\Scripts\python test_server.py
```

## Workflow Cursor - Crea MCP in 3 Step

Se usi **Cursor**, abbiamo ottimizzato il workflow con comandi rapidi accessibili tramite `/`:

### Step 1: Setup → `@Installazione_Progetto.md`
Installa MCP Builder e verifica che tutto funzioni:
```bash
python mcp_builder.py --help
```

### Step 2: Ricerca → `@Super_Search.md`
Trova idee, documentazione e best practices usando sequential thinking + MCP deep research. Perfetto per:
- Esplorare API disponibili
- Trovare documentazione aggiornata
- Identificare pattern e soluzioni

### Step 3: Build → `@Creazione_MCP.md`
Crea il tuo server seguendo la guida completa con troubleshooting avanzato. Include:
- Configurazione MCP client (Cursor/Claude Desktop)
- Test automatici
- Debug avanzato

**Workflow completo:** Setup → Ricerca → Build = Server MCP funzionante in pochi minuti

## Features

- **Generazione automatica** server MCP Python/TypeScript
- **FastMCP framework** per performance elevate
- **Pydantic v2** validazione input type-safe
- **Test suite automatica** inclusa
- **Trasporti supportati:** stdio, HTTP, SSE
- **Ambiente virtuale** integrato (.venv)
- **Error handling robusto** e logging completo
- **Template production-ready** con struttura GitHub-ready

## Esempi

```bash
# Server GitHub
python mcp_builder.py --service github --python --transport stdio

# Server Weather API
python mcp_builder.py --service weather-api --python --transport http

# Server TypeScript
python mcp_builder.py --service my-service --typescript --transport sse
```

## Struttura Progetto Generato

```
your_service_mcp/
├── your_service_mcp.py      # Server principale
├── test_server.py           # Test automatici
├── requirements.txt         # Dipendenze
├── pyproject.toml          # Packaging moderno
├── README.md               # Documentazione
└── .venv/                  # Virtual environment
```

## Requirements

- Python 3.8+
- FastMCP, httpx, pydantic

## Architecture

**Core Components:**
- MCPBuilder: generazione automatica server
- Template System: template Python/TypeScript ottimizzati
- Validation Layer: Pydantic v2
- Test Suite: framework test automatico

**Design:** Production-ready, security-first, async/await, standards compliant

## Best Practices

Server generati includono:
- Validazione input con modelli Pydantic
- HTTP client async con httpx
- Type hints completi
- Gestione errori completa
- Configurazione environment-based
- Logging professionale

**PowerShell:** Testato con PowerShell 5 e 7+, UTF-8 support, cross-platform

## Support & Community

- **GitHub Issues:** Bug reports e feature requests
- **Documentazione:** Guide complete in `.cursor/commands/`
- **Contribuzioni:** Welcome! Consulta le guide per contribuire

## License

MIT License - see LICENSE file for details.

---

**Project Founder:** MIC | **Version:** 1.0.0 | **Status:** Production Ready

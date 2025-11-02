# Creazione MCP Server - Guida Completa

## Sintassi PowerShell Windows

**IMPORTANTE:** In PowerShell Windows NON usare `&&` per concatenare comandi. Usare `;` o comandi separati.

```powershell
# SBAGLIATO:
cd "C:\path" && python mcp_builder.py --service example --python

# CORRETTO:
cd "C:\path"; python mcp_builder.py --service example --python

# OPPURE (comandi separati):
cd "C:\path"
python mcp_builder.py --service example --python
```

## Processo Completo

### 1. Genera server MCP:
```powershell
python mcp_builder.py --service SERVICE_NAME --python
```

### 2. Naviga nella directory generata:
```powershell
cd SERVICE_NAME_mcp
```

### 3. **OBBLIGATORIO: Crea e configura ambiente virtuale:**
```powershell
# Crea ambiente virtuale
python -m venv .venv

# Attiva ambiente virtuale
# PowerShell:
.venv\Scripts\Activate.ps1

# CMD:
.venv\Scripts\activate.bat

# macOS/Linux:
source .venv/bin/activate
```

### 4. **OBBLIGATORIO: Installa dipendenze:**
```powershell
pip install -r requirements.txt
```

### 5. **OBBLIGATORIO: Testa il server:**
```powershell
.venv\Scripts\python test_server.py
```

**ATTENDI:** L'output dovrebbe mostrare:
```
[OK] Server imports successfully
[OK] FastMCP server initialized: SERVICE_NAME_mcp
[OK] All basic tests passed!
```

## Configurazione in Cursor/Claude Desktop

### File di configurazione MCP

Trova il file di configurazione MCP:
- **Cursor:** `%APPDATA%\Cursor\User\globalStorage\mcp.json`
- **Claude Desktop:** `%APPDATA%\Claude\mcp.json`

### Configurazione corretta per il server

Aggiungi questa configurazione (CRUCIALE: includi `cwd`):

```json
{
  "mcpServers": {
    "SERVICE_NAME": {
      "command": "C:\\path\\to\\SERVICE_NAME_mcp\\.venv\\Scripts\\python.exe",
      "args": [
        "SERVICE_NAME_mcp.py"
      ],
      "cwd": "C:\\path\\to\\SERVICE_NAME_mcp",
      "env": {
        "API_KEY": "your-api-key-here"
      }
    }
  }
}
```

**IMPORTANTE:** 
- `cwd` (current working directory) è OBBLIGATORIO
- I percorsi devono usare doppi backslash `\\` su Windows
- Il percorso nel `command` deve essere assoluto al file python.exe
- Il percorso nel `args[0]` deve essere relativo al `cwd`

### Esempio concreto per holidays_mcp:

```json
{
  "mcpServers": {
    "holidays": {
      "command": "C:\\path\\to\\holidays_mcp\\.venv\\Scripts\\python.exe",
      "args": [
        "holidays_mcp.py"
      ],
      "cwd": "C:\\path\\to\\holidays_mcp",
      "env": {
        "HOLIDAYS_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Verifica Funzionamento

### 1. Riavvia il client MCP (Cursor/Claude Desktop)

**IMPORTANTE:** Chiudi completamente l'applicazione e riaprila.

### 2. Verifica che il server appaia

Il server dovrebbe apparire con i suoi tool disponibili.

### 3. Test rapido

Prova una query semplice per verificare il funzionamento:
- Per holidays: "Festività italiane del 1° novembre 2025"
- Per altri servizi: usa esempi appropriati

## Opzioni Disponibili per mcp_builder.py

```powershell
# Genera server Python
python mcp_builder.py --service SERVICE_NAME --python

# Specifica transport type
python mcp_builder.py --service SERVICE_NAME --python --transport stdio

# Escludi evaluation.xml
python mcp_builder.py --service SERVICE_NAME --python --no-evaluation

# Transport options: stdio, sse, http (default: stdio)
```

## Struttura Generata

Ogni progetto MCP generato e' completamente indipendente e include:

```
SERVICE_NAME_mcp/
├── SERVICE_NAME_mcp.py      # Server principale con tool MCP
├── test_server.py           # Suite test per verificare funzionamento
├── requirements.txt         # Dipendenze Python
├── pyproject.toml           # Packaging moderno Python
├── README.md                # Documentazione completa
├── LICENSE                  # MIT License
├── CHANGELOG.md            # Changelog del progetto
├── .gitignore              # Git ignore patterns
├── .venv/                   # Ambiente virtuale (da creare manualmente)
└── evaluation.xml          # Valutazione (se richiesta)
```

## Implementazione Custom

### 1. Implementa la logica API

Apri il file server: `SERVICE_NAME_mcp.py`

Aggiungi le tue implementazioni nei tool functions generati:
```python
@mcp.tool(...)
async def service_name_list_resources(params: ServiceNameListResourcesInput) -> str:
    # TODO: Implementa la logica API qui
    # Usa httpx per chiamate HTTP asincrone
    # Gestisci errori con _handle_api_error()
    # Restituisci JSON formattato
```

### 2. Aggiungi autenticazione

Per API keys, OAuth, etc.:
```python
# Nel server MCP
API_KEY = os.getenv("SERVICE_API_KEY", "fallback_key")

# Oppure nel file .env
# SERVICE_API_KEY=your-actual-key
```

### 3. Test approfondito

Aggiungi test specifici per la tua implementazione:

```powershell
# Test diretto del server
.venv\Scripts\python SERVICE_NAME_mcp.py

# Test da client MCP
# Prova le query previste
```

## Best Practices Include

- FastMCP framework per performance ottimali
- Pydantic v2 per validazione input robusta con errori chiari
- httpx async per operazioni HTTP asincrone efficienti
- Error handling completo con mapping HTTP
- Type hints completi per type safety
- MCP annotations per metadata LLM
- Logging di debug integrato

## Troubleshooting Approfondito

### ❌ "Server trovato ma senza tools"

**Causa:** Server si connette ma non espone strumenti MCP.

**Soluzioni:**
1. Verifica che l'ambiente virtuale esista e sia configurato
2. Testa il server: `.venv\Scripts\python test_server.py`
3. Aggiungi logging di debug al server se necessario
4. Verifica che `cwd` sia configurato correttamente nel MCP JSON

### ❌ "ModuleNotFoundError"

**Causa:** Dipendenze non installate nell'ambiente virtuale.

**Soluzione:**
```powershell
# Ricrea l'ambiente virtuale
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### ❌ "Impossibile trovare il percorso specificato"

**Causa:** Percorsi errati nel file di configurazione MCP JSON.

**Soluzione:**
1. Verifica che tutti i percorsi esistano
2. Usa percorsi assoluti per il comando
3. Usa percorsi relativi per gli argomenti (relativi al `cwd`)
4. Verifica che `cwd` sia specificato

### ❌ "Server si connette ma non risponde"

**Causa:** Server MCP non avviato correttamente.

**Soluzioni:**
1. Testa l'avvio diretto: `.venv\Scripts\python SERVICE_NAME_mcp.py`
2. Verifica che tutte le dipendenze siano installate
3. Controlla i log del client per errori
4. Aggiungi print di debug all'avvio del server

### ❌ Encoding Errors (charmap)

**Causa:** Caratteri Unicode/Emoji nel terminale Windows.

**Soluzione:**
- Evita emoji nella console
- Usa ASCII per output da terminale
- Verifica encoding dei file: UTF-8

### ❌ PowerShell Concatenation

**Causa:** Uso di `&&` in PowerShell.

**Soluzione:**
- Usa `;` per concatenare comandi
- O esegui comandi separati su righe diverse

## Debugging Avanzato

### 1. Abilita logging nel server

Aggiungi debug output all'avvio del server:
```python
if __name__ == "__main__":
    import sys
    print(f"[DEBUG] Starting {service_name} server", file=sys.stderr, flush=True)
    print(f"[DEBUG] Working directory: {os.getcwd()}", file=sys.stderr, flush=True)
    mcp.run(transport="stdio")
```

### 2. Test API diretto

Prima di usare il server MCP, testa l'API direttamente:
```python
# Crea script test_api.py per verificare che l'API funzioni
import requests

response = requests.get("https://api.example.com/endpoint", params={"key": "value"})
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
```

### 3. Test del server MCP

Usa un client MCP per testare:
```bash
# Test stdio connection
echo '{"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}' | python SERVICE_NAME_mcp.py
```

### 4. Verifica ambiente virtuale

```powershell
# Verifica che l'ambiente virtuale funzioni
.venv\Scripts\python --version
.venv\Scripts\pip list

# Test import
.venv\Scripts\python -c "import SERVICE_NAME_mcp; print('Import OK')"
```

## Checklist Pre-Produzione

Prima di considerare il server pronto per l'uso:

- [ ] Ambiente virtuale creato e funzionante
- [ ] Dipendenze installate correttamente
- [ ] Test del server: `test_server.py` passa tutti i test
- [ ] Test dell'API diretto (senza MCP) funziona
- [ ] Configurazione MCP JSON corretta con `cwd`
- [ ] Server appare nel client con tools visibili
- [ ] Test di una query funziona end-to-end
- [ ] Logging di debug rimosso (se necessario)
- [ ] Documentazione aggiornata

## Supporto e Risorse

- **FastMCP Documentation:** https://gofastmcp.com
- **MCP Protocol:** https://modelcontextprotocol.io
- **Troubleshooting:** Verifica sempre i log del client MCP
- **Template:** Usa mcp_builder.py per generare server standard

---

**Progetto generato con MCP Builder** - Best practices e troubleshooting avanzato incluso.
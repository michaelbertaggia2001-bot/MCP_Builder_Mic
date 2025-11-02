# Installazione MCP Builder

## Requisiti

- Python >= 3.10
- pip (Python package installer)
- Git (opzionale, per clonare repository)

## Installazione Locale

### 1. Clona o scarica il progetto

```powershell
# Se hai Git:
git clone <repository-url>
cd "MCP Builder"

# OPPURE: scarica e estrai il progetto
```

### 2. Verifica Python

```powershell
python --version
# Deve essere Python 3.10 o superiore
```

### 3. Installa dipendenze

```powershell
pip install mcp[cli] pydantic httpx python-dotenv
```

O crea un `requirements.txt` e installa:

```powershell
# Crea requirements.txt con:
mcp[cli]>=1.0.0
pydantic>=2.0.0
httpx>=0.28.0
python-dotenv>=1.0.0

# Poi installa:
pip install -r requirements.txt
```

## Verifica Installazione

### Test rapido

```powershell
python mcp_builder.py --help
```

Dovresti vedere l'help del comando.

### Genera server di test

```powershell
python mcp_builder.py --service test --python
```

Verifica che sia stata creata la directory `test_mcp` con tutti i file.

**IMPORTANTE:** Prima di testare il server generato, devi installare le dipendenze nell'ambiente virtuale:

```powershell
cd test_mcp
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python test_server.py
```

## Dipendenze del Progetto

MCP Builder richiede le seguenti dipendenze Python:

- **mcp[cli]**: Framework FastMCP per server MCP
- **pydantic**: Validazione dati e modelli (v2)
- **httpx**: Client HTTP asincrono (opzionale, usato nei template generati)
- **python-dotenv**: Gestione variabili ambiente (opzionale)

## Struttura del Progetto

```
MCP Builder/
├── mcp_builder.py              # Script principale
├── README.md                    # Documentazione progetto
├── .cursor/
│   └── commands/
│       ├── Creazione_MCP.md    # Command per creare MCP
│       └── Installazione_Progetto.md  # Questo file
└── requirements.txt            # Dipendenze (da creare se necessario)
```

## Uso Dopo Installazione

Dopo l'installazione, puoi usare MCP Builder per generare server MCP:

```powershell
# Genera un nuovo server MCP
python mcp_builder.py --service your-service --python

# Naviga nella directory generata
cd your-service_mcp

# Attiva ambiente virtuale (creato automaticamente)
.venv\Scripts\Activate.ps1

# Installa dipendenze nel progetto generato
pip install -r requirements.txt

# Testa il server generato
.venv\Scripts\python test_server.py
```

## Troubleshooting

### Python non trovato

```powershell
# Verifica installazione Python
python --version

# Se non funziona, prova:
py --version

# Aggiungi Python al PATH se necessario
```

### Errore installazione dipendenze

```powershell
# Aggiorna pip
python -m pip install --upgrade pip

# Installa una dipendenza alla volta per identificare problemi
pip install mcp[cli]
pip install pydantic
pip install httpx
pip install python-dotenv
```

### Errore encoding

Se vedi errori di encoding, assicurati che i file siano salvati in UTF-8.

### Permission denied (venv)

Su Windows, potrebbe essere necessario eseguire PowerShell come amministratore per creare venv.

### Errore "No module named 'httpx'" o moduli mancanti

Questo errore si verifica se provi a testare il server senza aver installato le dipendenze nell'ambiente virtuale del progetto generato.

**Soluzione:**
```powershell
# Assicurati di essere nella directory del progetto MCP generato
cd SERVICE_NAME_mcp

# Installa le dipendenze nell'ambiente virtuale
.venv\Scripts\python -m pip install -r requirements.txt

# Ora puoi testare
.venv\Scripts\python test_server.py
```

**Nota:** L'ambiente virtuale `.venv` del progetto generato e' isolato e richiede l'installazione delle dipendenze anche se le hai gia' installate globalmente.

## Aggiornamento

Per aggiornare le dipendenze:

```powershell
pip install --upgrade mcp[cli] pydantic httpx python-dotenv
```

## Supporto

Per problemi o domande, consulta:
- Documentazione FastMCP: https://gofastmcp.com
- README.md del progetto
- Issues su GitHub (se disponibile)

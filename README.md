# research

Minimal FastAPI backend skeleton with:
- config via environment variables / `.env`
- structured logs via `structlog`
- APIs organized using routers (`research/routes/`)

## Run

From the venv:

```powershell
python main.py
```

Or directly:

```powershell
uvicorn research.app:app --reload
```


## Example API

```bash
curl -X POST http://127.0.0.1:8000/api/agent/echo \
	-H "Content-Type: application/json" \
	-d '{"message":"hi"}'
```

## Config

Environment variables (optional):
- `APP_NAME` (default: `research`)
- `APP_ENV` (`development` | `test` | `production`, default: `development`)
- `LOG_LEVEL` (default: `INFO`)
- `HOST` (default: `127.0.0.1`)
- `PORT` (default: `8000`)
- `RELOAD` (default: `true` in development)


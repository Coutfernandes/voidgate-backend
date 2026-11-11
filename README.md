# voidgate-backend

API da **VoidGate**, a camada de segurança entre aplicações e modelos de IA.

Frontend: [VoidGates/voidgate-frontend](https://github.com/VoidGates/voidgate-frontend)

## Stack

Python 3.12+ + FastAPI

## Rodando

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate   |   Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload   # http://localhost:8000  (docs em /docs)
```

## Testes

```bash
pytest
```

## Estrutura

```
app/
  main.py      # ponto de entrada, rotas
tests/         # testes com pytest
```

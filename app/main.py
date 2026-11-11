from fastapi import FastAPI

app = FastAPI(title="VoidGate API")


@app.get("/health")
def health():
    return {"status": "ok"}

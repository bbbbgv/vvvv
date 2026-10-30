from fastapi import FastAPI, HTTPException
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"ok": True}

@app.get("/proxy")
def proxy(target_url: str):
    headers = {
        "User‑Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Accept‑Language": "zh‑CN,zh;q=0.9"
    }
    try:
        resp = requests.get(target_url, headers=headers, timeout=25)
        return {
            "ok": True,
            "code": resp.status_code,
            "text": resp.text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI, Request
import random

all_emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🦝", "🐻", "🐼", "🐨", "🐯",
              "🦁", "🐮", "🐷", "🐽", "🐸", "🐵", "🙈", "🙉", "🙊", "🐒", "🦍", "🦧", "🦮", "🐕",
              "🐩", "🐺", "🦊", "🦝", "🐈", "🐈‍⬛", "🐅", "🐆", "🦓", "🦌", "🦬", "🐂", "🐃", "🐄",
              "🐎", "🦄", "🐖", "🐗", "🐏"]

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

@app.post("/api/py/message")
async def predict_emojis(request: Request):
    body = await request.json()
    print(body)
    return {"emojis": random.sample(all_emojis, 3)}
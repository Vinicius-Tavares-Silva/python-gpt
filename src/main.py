import uvicorn
from fastapi import FastAPI

from .routers import chat, transcription


app = FastAPI()

app.include_router(chat.router)
app.include_router(transcription.router)

if __name__ == "__main__":
  uvicorn.run(app, port=8080)

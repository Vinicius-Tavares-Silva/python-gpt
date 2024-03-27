from fastapi import APIRouter
from pydantic import BaseModel

from src.services import ai_client

class Payload(BaseModel):
  message: str

router = APIRouter(
  prefix="/chat",
  tags=["chat"],
)

gpt = ai_client.AiClient()


@router.post('/')
async def conversation(payload: Payload):
  messages = gpt.chat_generation(message=payload.message)
  return messages

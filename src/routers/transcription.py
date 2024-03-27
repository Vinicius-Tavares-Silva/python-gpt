from fastapi import APIRouter
from pydantic import BaseModel

from src.services import ai_client

class Payload(BaseModel):
  file_path: str

router = APIRouter(
  prefix="/transcription",
  tags=["transcription"],
)

gpt = ai_client.AiClient()


@router.post('/')
async def get_transcription(payload: Payload):
  gpt_transcription = gpt.transcription_speech(path=payload.file_path)
  return { 'gpt_transcription': gpt_transcription }

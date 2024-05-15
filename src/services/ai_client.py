from openai import OpenAI

CHAT_MODEL = 'gpt-3.5-turbo'
TRANSCRIPTION_MODEL = 'whisper-1'
API_KEY = 'API_KEY'

class AiClient:

  def __init__(self) -> None:
    self.client = OpenAI(api_key=API_KEY)

  def chat_generation(self, message: list = None) -> str:
    format_message = { "role": "user", "content": message }
    response = self.client.chat.completions.create(
      model=CHAT_MODEL,
      messages=[format_message]
    )
    return {
      'user_message': message,
      'gpt_message': response.choices[0].message.content
    }

  def transcription_speech(self, path: str = None) -> str:
    audio_file= open(path, 'rb')
    transcription = self.client.audio.transcriptions.create(
      model=TRANSCRIPTION_MODEL,
      file=audio_file
    )
    return transcription.text

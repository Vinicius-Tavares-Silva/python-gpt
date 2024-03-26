from openai import OpenAI

CHAT_MODEL = 'gpt-3.5-turbo'
TRANSCRIPTION_MODEL = 'whisper-1'
API_KEY = 'sess-WzEmppv3c5dJa7f7mzdZ0kQ7B447fbfsgWKpTP12'

class AiClient:

  def __init__(self) -> None:
    self.client = OpenAI(api_key=API_KEY)

  def chat_generation(self, messages) -> dict:
    response = self.client.chat.completions.create(
      model=CHAT_MODEL,
      messages=messages
    )
    return response

  def transcription_speech(self, path) -> dict:
    audio_file= open(path, 'rb')
    transcription = self.client.audio.transcriptions.create(
      model=TRANSCRIPTION_MODEL,
      file=audio_file
    )
    return transcription

# print('Vamos la!')
# gpt = AiClient()

# messages = [
#   {"role": "user", "content": "Ola, tudo bom?"}
# ]

# chat = gpt.chat_generation(messages)
# print(chat.choices[0].message.content)

# audio_transcription = gpt.transcription_speech("/mnt/c/Users/Vini_/Downloads/audio_test.mp3")
# print(audio_transcription)

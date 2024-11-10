from utils.mistral_ai import mistral_ai
from TTS.api import TTS

tts = TTS('tts_models/en/ljspeech/tacotron2-DDC_ph')
tts.to('cuda')
gpt = mistral_ai()


user_input = open('./input.txt')
user_text = user_input.read()
res = gpt.chat_completion('Explain this in a better way to understand (with no punctuations please, only text)\n'+user_text,3)
tts.tts_to_file(res)
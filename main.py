from utils.mistral_ai import mistral_ai
from TTS.api import TTS
from flask import Flask, render_template, request, send_from_directory
import os


app = Flask(__name__)
tts = TTS('tts_models/en/ljspeech/tacotron2-DDC_ph')
tts.to('cuda')
gpt = mistral_ai()

@app.route("/", methods=["GET", "POST"])
def index():
	is_audio_file = False
	if request.method == "POST":
        # Get text input
		user_text = request.form["text_input"]
		res = gpt.chat_completion('Explain this in a better way to understand (with no punctuations please, only text)\n'+user_text,3)
		tts.tts_to_file(res,file_path='./static/output.wav')
		is_audio_file = True

		return render_template("index.html", audio_file=is_audio_file)
	return render_template("index.html", audio_file=is_audio_file)

@app.route("/static/<filename>")
def serve_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == "__main__":
    app.run(debug=True)
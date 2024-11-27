from utils.mistral_ai import mistral_ai
from gtts import gTTS
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
gpt = mistral_ai()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get text input
        user_text = request.form["text_input"]
        res = gpt.chat_completion('Explain this in a better way to understand (with no punctuations please, only text)\n'+user_text, 3)
        
        # Save the audio file
        gTTS(res).save("./static/output.wav")
        
        # Redirect to the audio page
        return redirect(url_for('audio'))

    return render_template("index.html")

@app.route("/audio")
def audio():
    # Pass the filename to the template to be used in the audio player
    return render_template("audio.html", filename='output.wav')

@app.route("/static/<filename>")
def serve_file(filename):
    # Make sure the path is correctly referenced
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == '__main__':
    # Get the port from the environment variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

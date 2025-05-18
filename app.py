from flask import Flask, render_template, send_from_directory
from mic_detector import MicDetector

app = Flask(__name__)
detector = MicDetector()
detector.start()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/status")
def status():
    return "open" if detector.is_active() else "close"

@app.route("/image")
def image():
    image_name = "open.png" if detector.is_active() else "close.png"
    return send_from_directory("static", image_name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=25226)
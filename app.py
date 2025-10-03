from flask import Flask, request, render_template
from ascii_converter import image_to_ascii
import os 
import tempfile

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return "No File Uploaded", 400
    
    file =request.files["image"]

    if file.filename == "":
        return "No Selected File", 400
    
    filepath = os.path.join("images", file.filename)
    file.save(filepath)

    ascii_art = image_to_ascii(filepath, new_width=100)
    print(ascii_art[:200])
    return render_template("result.html", ascii_art=ascii_art)

if __name__ == "__main__":
    app.run(debug=True)
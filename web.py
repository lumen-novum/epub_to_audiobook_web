from flask import request, render_template, Flask
from main import main

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_ebook():
    f = request.files['ebook']
    f.save(f.filename)
    try:
        main(f.filename)
    except:
        return '<script>alert("Upload failed! See terminal for more details.");</script>'
    
    return '<script>alert("Conversion successful!");</script>'
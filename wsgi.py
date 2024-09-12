from flask import request, render_template, Flask
from os import remove, path, mkdir

import main


app = Flask(__name__)

# Show index page when accessed through browser
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Handle POST upload request
@app.route('/', methods=['POST'])
def upload_ebook():
    f = request.files['ebook']

    # Save e-book file
    work_folder = '../books/' + path.splitext(f.filename)[0] 
    input_path = work_folder + "/" + f.filename

    try:
        mkdir(work_folder)
    except FileExistsError:
        pass # Ignore if folder already exists

    f.save(input_path)

    try:
        # Convert audio book and get base file name
        main.main(input_path, work_folder)
    except:
        return '<script>alert("Conversion failed! See terminal for more details.");</script>'
    
    return '<script>alert("Conversion successful!");</script>'
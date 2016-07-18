import os
from io import BytesIO
from werkzeug.datastructures import FileStorage
from flask import Flask, request, url_for, send_from_directory, jsonify
app = Flask(__name__)
from werkzeug.utils import secure_filename
import base64

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(APP_ROOT, UPLOAD_FOLDER)


@app.route('/')
def main():
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <div>
        <input id=input type=file name=file>
        <button id="upload">upload</button>
    </div>
    <canvas id='c'></canvas>
    <img id='result'></img>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/fabric.js/1.6.3/fabric.js"></script>
    <script src="static/script.js"></script>
    '''


@app.route('/upload_banner', methods=['POST'])
def upload_banner():
    _, b64data = request.json['file'].split(',')
    decoded_data = base64.b64decode(b64data)
    file = FileStorage(BytesIO(decoded_data), filename='banner.jpg')
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({'src': url_for('uploads', filename=filename)})


@app.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
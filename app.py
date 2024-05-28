from flask import Flask, request, render_template, redirect, url_for
import zipfile
import os
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and file.filename.endswith('.zip'):
        return handle_zip_file(file)

    return 'Invalid file format. Please upload a ZIP file.'

def handle_zip_file(file):
    zip_ref = zipfile.ZipFile(file, 'r')
    extracted_files = {}

    for file_info in zip_ref.infolist():
        if file_info.is_dir():
            continue
        with zip_ref.open(file_info.filename) as f:
            content = f.read().decode('utf-8')
            extracted_files[file_info.filename] = content
    
    return render_template('display_files.html', files=extracted_files)

if __name__ == '__main__':
    app.run(debug=True)

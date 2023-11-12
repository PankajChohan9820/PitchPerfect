# app.py

from flask import Flask, request, jsonify, stream_with_context, Response
from helper import scraper, get_gpt, pdf_save
from os import makedirs, path
import json
from flask_cors import CORS, cross_origin
import sys
import os

# Add the parent directory of the backend folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


with open('prompts.json', 'r') as file:
    # Load the JSON data into a Python dictionary
    data = json.load(file)


with open('mock_data.json', 'r') as file:
    # Load the JSON data into a Python dictionary
    mock_data = json.load(file)

# Dummy user data (replace with a database or proper user authentication)
valid_users = {
    'pankajchohan9820@gmail.com': 'qwerty123',
    'user2': 'password2'
}

app = Flask(__name__)
CORS(app)

# Define the directory where uploaded PDFs will be saved
UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return 'Hello, Flask!'



@app.route('/scrape', methods=['POST'])
def scrape_url():
    try:
        # url = request.args.get('url')
        url = 'https://www.linkedin.com/jobs/search/?currentJobId=3757039507'
        if not url:
            return jsonify({'error': 'URL parameter is missing'}), 400


        result = mock_data['mock_data']

        # result = scraper.scrap_data(url)
        result = get_gpt.askgpt(data['extract_role'] + str(result))
        my_resume = pdf_save.extract_pdf()

        return Response(stream_with_context(get_gpt.generate( data['role_play'], my_resume, data['test_2'] + ' ' + result )), content_type='text/plain')
        
    except Exception as e:
        response_data = {'status': 'error', 'message': str(e)}
        return jsonify(response_data), 500




@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    try:
        # Check if a PDF file is included in the request
        if 'resume' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        pdf_file = request.files['resume']

        # Check if the file is empty
        if pdf_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Check if the file has a valid PDF extension
        if not pdf_file.filename.endswith('.pdf'):
            return jsonify({'error': 'Invalid file format. Only PDF files are allowed'}), 400

        # Create the uploads directory if it doesn't exist
        makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

        # Save the uploaded PDF to the uploads directory
        pdf_file.save(path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename))
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        response_data = {'status': 'error', 'message': str(e)}
        print(str(e))
        return jsonify(response_data), 500



@app.route('/login-check', methods=['POST'])
def login_check():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Check if the username and password are correct
        if username in valid_users and valid_users[username] == password:
            response_data = {'status': 'correct', 'message': 'Login successful'}
            return jsonify(response_data), 200
        else:
            response_data = {'status': 'not okay', 'message': 'Invalid credentials'}
            return jsonify(response_data), 401

    except Exception as e:
        response_data = {'status': 'error', 'message': str(e)}
        return jsonify(response_data), 500


# handler = Mangum(app)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
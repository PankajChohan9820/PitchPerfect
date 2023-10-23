from flask import Flask, request, jsonify
from helper import scraper
from os import makedirs, path


app = Flask(__name__)

# Define the directory where uploaded PDFs will be saved
UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return 'Hello, Flask!'

@app.route('/scrape', methods=['GET'])
def scrape_url():

    # url = request.args.get('url')
    url = 'https://www.linkedin.com/jobs/search/?currentJobId=3712601062'
    if not url:
        return jsonify({'error': 'URL parameter is missing'}), 400

    res = scraper.scrap_data(url)
    # print("Res",res)

    if not res:
        return jsonify({'error': 'There is no data'}), 400
    
    return jsonify({'Responsibilities': res}), 200


@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    print('Hello', request.files)
    # Check if a PDF file is included in the request
    if 'resume' not in request.files:
        print('1')
        return jsonify({'error': 'No file part'}), 400

    pdf_file = request.files['resume']

    # Check if the file is empty
    if pdf_file.filename == '':
        print('2')
        return jsonify({'error': 'No selected file'}), 400

    # Check if the file has a valid PDF extension
    if not pdf_file.filename.endswith('.pdf'):
        print('3')
        return jsonify({'error': 'Invalid file format. Only PDF files are allowed'}), 400

    # Create the uploads directory if it doesn't exist
    makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Save the uploaded PDF to the uploads directory
    pdf_file.save(path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename))


    return jsonify({'message': 'File uploaded successfully'}), 200




if __name__ == '__main__':
    app.run()

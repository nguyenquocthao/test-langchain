from flask import Flask, request, jsonify
from caption import captionImage

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    # Process the uploaded file
    # Here, you can perform actions like saving the file, processing its contents, etc.
    # In this example, we'll just return the filename and size as a JSON response

    caption = captionImage(file)
    print(20, caption)

    filename = file.filename

    return jsonify({'filename': filename, 'size': request.content_length, 'cap': caption.page_content, **caption.metadata})

@app.route("/")
def helloworld():
    return 'Hello world'

if __name__ == '__main__':
    app.run()
# This creates a basic flask web server for the smart home pi, the server allows users to upload files and stores them in the project storage folder.
# Features:
# - upload files
# - list stored files
# - download files


import os
from flask import Flask, request, send_from_directory

# Create flask application instance
app = Flask(__name__)

# Define where uploaded files will be saved
UPLOAD_FOLDER = "/mnt/hdd"

# Create the storage fodler if it does not already exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Define route for homepage
@app.route("/")
def home():
    # Get list of files from storage
    files = os.listdir(UPLOAD_FOLDER)

    # Build HTML page with a list of files
    file_list_html = ""
    for file in files:
        file_list_html += f'<li><a href="/download/{file}">{file}</a></li>'

    return """
    <h1>Smart Home Cloud Pi</h1>
    <h2>Upload File</h2>

    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>

    <h2>Stored Files</h2>
    <ul>
        {file_list_html}
    </ul>
    """

# Upload route
@app.route("/upload", methods=["POST"])
def upload_file():
    # Check if the request contains a file
    if "file" not in request.files:
        return "No file selected"

    file = request.files["file"]

    # Check if the file has a name
    if file.filename == "":
        return "No file selected"

    # Create the full save path inside the storage folder
    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    # Save the uploaded file to the Raspberry Pi
    file.save(save_path)

    return f"File '{file.filename}' uploaded successfully <br><a href='/'>Back</a>"

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

# Run the Flask app
if __name__ == "__main__":
    # host="0.0.0.0" allows other devices on the WiFi network to access the app
    app.run(host="0.0.0.0", port=5000)
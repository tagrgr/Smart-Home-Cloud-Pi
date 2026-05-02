# This creates a basic flask web server for the smart home pi
# The server allows users to upload files and stores them in the project storage folder.

import os
from flask import Flask, request

# Create flask application instance
app = Flask(__name__)

# Define where uploaded files will be saved
UPLOAD_FOLDER = "storage"

# Create the storage fodler if it does not already exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Define route for homepage
@app.route("/")
def home():
    # Return a simple HTML page with a file upload form
    return """
    <h1>Smart Home Cloud Pi</h1>
    <p>Upload a file to your Raspberry Pi cloud storage.</p>

    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
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

    return f"File '{file.filename}' uploaded successfully"

# Run the Flask app
if __name__ == "__main__":
    # host="0.0.0.0" allows other devices on the WiFi network to access the app
    app.run(host="0.0.0.0", port=5000)
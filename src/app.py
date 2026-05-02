# This creates a basic flask web server for the smart home pi

from flask import Flask

# Create flask application instance
app = Flask(__name__)

# Define route for homepage
@app.route("/")
def home():
    # This function runs when user gets to the root URL
    return "Smart Home Cloud Pi is running"

# Run the application
if __name__ == "__main__":
    # Run server on all network interfaces so other devices can access
    app.run(host="0.0.0.0", port=5000)
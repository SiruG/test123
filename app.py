from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello_siru_flaskapp():
    return 'Hello Siru Flaskapp!'

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5002)

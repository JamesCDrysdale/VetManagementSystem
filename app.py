from flask import Flask

# Create application object as an instance of class Flask
app = Flask(__name__)

from controllers import controller

if __name__ == '__main__':
    app.run(debug=True)

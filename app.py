from flask import Flask, render_template
from controllers.clients_controller import clients_blueprint

# Create application object as an instance of class Flask
app = Flask(__name__)

app.register_blueprint(clients_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

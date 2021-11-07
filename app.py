from flask import Flask, render_template
from controllers.brand_controller import brand_blueprint
from controllers.keyboard_controller import keyboard_blueprint
from models.keyboard import Keyboard

app = Flask(__name__)

app.register_blueprint(brand_blueprint)
app.register_blueprint(keyboard_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
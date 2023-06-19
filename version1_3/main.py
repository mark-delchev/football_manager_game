from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    names = generate_names()  # Replace generate_names() with your own function
    return render_template('index.html', names=names)

def generate_names():
    # Your code to generate random names
    names = ['Alice', 'Bob', 'Charlie']  # Replace with your actual name generation logic
    return names

if __name__ == '__main__':
    app.run(debug=True)

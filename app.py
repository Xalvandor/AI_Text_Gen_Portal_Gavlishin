import random
import sys

from flask import Flask, jsonify, send_from_directory, render_template
import subprocess
import torch

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate_text():
    result = subprocess.run(
        [
            sys.executable, 'sample.py', f'--seed={random.randint(0,2000)}',
        ],
        capture_output=True, text=True
    )
    return jsonify({"output": result.stdout.strip()})

if __name__ == '__main__':
    app.run(debug=True)


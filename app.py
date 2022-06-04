from flask import Flask, render_template, request, jsonify
import joblib
import tensorflow as tf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def heart_segmentation():
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
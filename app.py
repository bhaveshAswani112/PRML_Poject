from flask import Flask, request, jsonify , send_file
from output import finalOutput


app = Flask(__name__)

@app.route('/')
def home():
    return send_file("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    sentence = request.form['text']
    sentiment = finalOutput(sentence)
    return jsonify({'sentiment': sentiment})
    


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, jsonify, request
from agent1 import run_conversation
from audio1 import text_audio

app = Flask(__name__)

@app.route('/process_message', methods=['POST'])
def process_message_func1():
    msg=request.json['message']
    print(msg)
    resp = run_conversation(msg)
    text_audio(resp)
    return jsonify({"response": resp })

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
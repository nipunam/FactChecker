from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
#import FactChecker

app = Flask(__name__, static_url_path='/static')

questions = []

@app.route('/hello/')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/hello/answers/')
def answers():
    return jsonify(questions)

@app.route('/hello/answer/')
def answer():
    question = request.args.get('question')
    answer = "answer" 
    # FactChecker.FactChecker.find_answer(question)
    response = { "question": question, "answer": answer}
    questions.append(response)
    return jsonify(response)


if __name__ == "__main__":
    app.run()
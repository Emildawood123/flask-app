from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)

JOPS = [
    {
        'id': 1,
        'jop': 'backend engineer',
        'company': 'google',
        'location': 'bangalore',
        'sallary': '5000$'
    },
    {
        'id': 2,
        'jop': 'frontend engineer',
        'company': 'facebook',
        'location': 'san fransico',
        'sallary': '3000$'
    },
    {
        'id': 3,
        'jop': 'data analyst',
        'company': 'amazon',
        'location': 'Cario',
        'sallary': '1500$'
    },
    {
        'id': 4,
        'jop': 'Doctor',
        'company': 'microsoft',
        'location': 'giza',
        'sallary': '1300$'
    },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jops=JOPS)


@app.route('/api/jops')
def list_jops():
  return jsonify(JOPS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return "Darlan Jr e zica"

@app.route('/contatos')
def contatos():
    return 'Nossos contatos sao: email -> junim@gmail.com'

if __name__ == "__main__":
    app.run(debug=True)
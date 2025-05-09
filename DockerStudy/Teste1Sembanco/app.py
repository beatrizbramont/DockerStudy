from flask import Flask

app1 = Flask(__name__)

@app1.route('/')
def ola():
    return ("Olá, to testando essa aplicação com Docker. Me deseje sorte!:)")

if __name__ == '__main__':
    app1.run(host='0.0.0.0', port=5000)
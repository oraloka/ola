from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Esquizofrenia total con este trabajo'

@app.route('/index')
def hola_adso():
    return 'Locura absoluta'

@app.route('/index2')
def hola_adso2():
    return 'Por fin sirvio esto'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000) 
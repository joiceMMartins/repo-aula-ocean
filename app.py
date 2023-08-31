from flask import Flask

app = Flask("meu app")

#@ é o decorator, que são funções que recebm funções como argumento
@app.route('/')
def hello():
    return "<p>Hello World</p>"

@app.route('/novo')
def novo():
    return "<h1> Nova página </h1>"
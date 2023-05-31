from flask import Flask

# essa instancia da classe flask é usada para lidar com requisições e resposta http
app = Flask(__name__)  #__name__ contem o nome do modulo python atual, nesse caso hello.py

# esse decorator transforma o retorno da função hello() resposta http que será exibidia pelo cliente (navegador)
@app.route('/')
def hello():
    return 'Hello, World!'
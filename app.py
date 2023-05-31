from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def teste_1():
    return "<h2> teste_1</h2>"

def teste_2():
    return "<h2> teste_2</h2>"

app.add_url_rule('/teste', 'teste_1', teste_1)

# Criando url dinâmica 

#essa rota mapeia a func_dinamica() para o valor default
@app.route('/hello')
@app.route('/hello/<nome>/<int:postID>')
@app.route('/hello/<nome>/')
def func_dinamica(nome='', postID= -1):

    if postID > 0:
        return f'esse é o meu numero da sorte: {postID}'
    else:
        return f'Olá, {nome}'

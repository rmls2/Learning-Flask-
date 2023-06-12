from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/',  methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        senha = request.form['senha']
        return render_template('botao.html', email=email, senha=senha)
@app.route('/botao/',  methods=["POST", "GET"])
def botao():
    resposta_email = request.form['email']
    resposta_senha = request.form['senha']

    return f'essa é {resposta_email} e {resposta_senha}'

    
def teste_1():
    return "<h2> teste_1</h2>"

def teste_2():
    return "<h2> teste_2</h2>"

# essa função mapeia a url /teste para o retorno da função teste_1 
app.add_url_rule('/teste', 'teste_2', teste_2)

# Criando url dinâmica - Aula 3 

#essa rota mapeia a func_dinamica() para o valor default
@app.route('/hello/')
@app.route('/hello/<nome>/<int:postID>')
@app.route('/hello/<nome>/')
def func_dinamica(nome='', postID= -1):  #os argumentos dentro dafunção decorada só virão daquilo que vem da URL

    if postID > 0:
        return f'esse é o meu numero da sorte: {postID}'
    else:
        return f'Olá, {nome}'
    
# construção de url - Aula 4 

@app.route('/admin/<adm_name>')
def admin(adm_name):
    return "oi, administrador %s."%adm_name 

@app.route('/guest/<guest_name>')
def guest(guest_name):
    return f"oi, usuário %s."%guest_name

@app.route ('/user/<name>/<adm_name>')
@app.route ('/user/<name>/')
def user (name, adm_name=''):
    if name == 'admin':
        return redirect(url_for('admin', adm_name = adm_name))
    else:
        return redirect(url_for('guest', guest_name = name))
    
# a função redirect() redireciona a url mapeada para uma url específica, nesse caso, paara o google.com
@app.route('/google')
def redirec_google():
    return redirect('https://www.google.com/') 

if __name__=='__main__':    
    app.run(debug=True)
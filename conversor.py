from flask import Flask, render_template, redirect, url_for, request
import platform
import subprocess
import os
import shutil


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-pdf')
def create_files_folder():
    global PDF_FOLDER 
    global TXT_FOLDER 
    # Cria os diretórios onde ficarão os arquivos caso ainda não existam
    if not os.path.exists('files'):
        os.makedirs('files/pdf')
        os.makedirs('files/txt') 

    # Diretórios onde ficarão armazenados os arquivos PDF e TXT conforme seu sistema operacional
    if platform.system() == "Linux":
        PDF_FOLDER = "files//pdf"
        TXT_FOLDER = "files//txt"
        
    elif platform.system() == "Windows":
        PDF_FOLDER = "files\\pdf"
        TXT_FOLDER = "files\\txt"
    else:
        print("Sistema operacional não reconhecido")
        exit()
    return render_template('conversao.html')

@app.route('/conversor', methods=['POST'])
def converter_file():
    # recupera o arquivo enviado no request usando o post
    arquivo = request.files['arquivo']
    #salva o nome do arquivo na variável filename
    filename = arquivo.filename

    # Salva o arquivo no sistema de arquivos
    arquivo.save(filename)

    # Move o arquivo para o diretório adequado
    shutil.move(filename, 'files/pdf/')

    # Cria o caminho do arquivo de texto
    dir_arq_conv = os.path.join('files/txt/', filename.replace(".pdf", ".txt"))

    # Executar o comando pdftotext para converter o texto, o resultado da execução é capturado com capture_output=True
    # Verifica se a conversão foi bem-sucedida, verificando o código de retorno do comando pdftotext usando .returncode.
    # Se for igual a 0, significa que a conversão foi concluída com sucesso
    if subprocess.run(['pdftotext', 'files/pdf/' + filename, dir_arq_conv], capture_output=True).returncode == 0:
        # Remover o arquivo PDF após a conversão 

        os.remove('files/pdf/' + filename)
        return '<h1>Convertido com sucesso</h1>'
    else:
        return 'A conversão falhou'

    """  if platform.system == 'Windows':
        if subprocess.run(['pdftotext', PDF_FOLDER+"\\"+filename, dir_arq_conv ], capture_output = True):
            os.remove(PDF_FOLDER+"\\"+filename)
    else:
        print("Sistema operacional não reconhecido")
        exit() """


app.run(debug=True)
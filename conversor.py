from flask import Flask, render_template, redirect, url_for, request
import platform
import subprocess
import os
import shutil


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diretorio')
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
    return render_template('diretorio.html')

@app.route('/conversor', methods=['POST'])
def converter_file():
    
    arquivo = request.files['arquivo']
    filename = arquivo.filename
     # Informa onde vai ficar o arquivo txt
    dir_arq_conv = os.path.join('files/pdf/', filename.replace(".pdf",".txt"))

    # Executa a ferramenta xpdf conforme o sistema operacional
    # pdftotext <arquivo pdf> <diretorio e o nome do arquivo a ser convertido>
    if platform.system == 'Linux':
        if subprocess.run(['pdftotext', 'files/pdf'+filename, dir_arq_conv ], capture_output = True):
        # os.remove(PDF_FOLDER+"//"+filename)
            return 'ok'
    return 'falhou'
    """  if platform.system == 'Windows':
        if subprocess.run(['pdftotext', PDF_FOLDER+"\\"+filename, dir_arq_conv ], capture_output = True):
            os.remove(PDF_FOLDER+"\\"+filename)
    else:
        print("Sistema operacional não reconhecido")
        exit() """

"""     st.write("Arquivo convertido com sucesso!")

    # Criando o botão de download
    with open(r""+dir_arq_conv , encoding="utf-8" , errors='ignore') as f:
        st.download_button(f'Baixar o arquivo', f, filename.replace(".pdf",".txt")) """

app.run(debug=True)
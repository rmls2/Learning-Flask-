from flask import Flask, render_template, redirect, url_for, request
import platform
import subprocess
import os
import shutil

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def conversor():
    if request.method == 'GET':
        return render_template('teste.html')
    else:
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


        # Converte o arquivo pdf para o formato txt.
        # Detecta em qual sistema operacional o script está rodando
        def conv_file(path, filename, sist_op):

            # Informa onde vai ficar o arquivo txt
            dir_arq_conv = os.path.join(TXT_FOLDER, filename.replace(".pdf",".txt"))

            # Executa a ferramenta xpdf conforme o sistema operacional
            # pdftotext <arquivo pdf> <diretorio e o nome do arquivo a ser convertido>
            if sist_op == 'Linux':
                if subprocess.run(['pdftotext', path+"//"+filename, dir_arq_conv ], capture_output = True):
                    os.remove(path+"//"+filename)
            elif sist_op == 'Windows':
                if subprocess.run(['pdftotext', path+"\\"+filename, dir_arq_conv ], capture_output = True):
                    os.remove(path+"\\"+filename)
            else:
                print("Sistema operacional não reconhecido")
                exit()

        



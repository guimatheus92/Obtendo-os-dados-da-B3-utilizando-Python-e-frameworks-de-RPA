
# Importa os módulos necessários para o script ser executado
import pandas as pd
import time
import datetime
import shutil
import os
import glob
import zipfile
import pathlib

from selenium import webdriver

# Define o nome do diretório onde está o arquivo baixado
src = pathlib.Path("D:\\Users\\F02579\\Downloads")

# Define o diretório aonde o arquivo será copiado após baixado
dst = pathlib.Path("D:\\Users\\F02579\\Documents")

# Recebe os arquivos do diretório na variavel
files = os.listdir(src)

# Verifica se possui algum arquivo com a extensão ZIP e TXT no diretório, e se estiver, deleta o arquivo
for file in files:
    if file.lower().endswith(('.zip', '.txt')):
        print(os.path.join(src, file))
        os.remove(os.path.join(src, file))

# A URL abaixo foi retirado do link do site
# http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-a-vista/codigo-isin/pesquisa/

# Coloque a URL abaixo
url = "https://sistemaswebb3-listados.b3.com.br/isinPage/#accordionBodyTwo"

# Para abrir o Chrome automaticamente, deve baixar o driver chromedriver de acordo com a versão da web instalado
options = webdriver.ChromeOptions()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--allow-running-localhost')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
executable_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

# A partir dessa etapa, ele virá fazer tudo automaticamente dentro do browser
# Abre o browser do Google Chrome automaticamente
browser = webdriver.Chrome(executable_path, options = options)

# Obtém os dados através da variavel URL
browser.get(url)

# Aguarda 10 segundos, para o link do site ser carregado antes de ser clicado automaticamente
time.sleep(10)

# Através do browser, ele clica no sinal de expandir o quadrante onde se encontra o item a ser clicavel
browser.find_element_by_xpath('//*[@id="accordionHeadingTwo"]/div/div/a').click()

# Aguarda 10 segundos, para o link do site ser carregado antes de ser clicado automaticamente
time.sleep(10)

# Através do browser ele clica no item que faz o download dos arquivos necessários. Através do titulo "Banco de Dados Completo"
browser.find_element_by_xpath('//*[@id="accordionBodyTwo"]/div/div[1]/div[1]/div[2]/p[1]/a').click()

# Adiciona 1 segundo enquanto o arquivo baixado com a extensão zip não constar no diretório, antes de fechar o browser
# Após ser baixado, adiciona o nome do arquivo para uma variável
while not glob.glob(str(src) + "\*.zip"):
    time.sleep(1)
else:
    print("Arquivo baixado do link " + str(url))

# Fecha o browser
browser.close()

# Aguarda 5 segundos, para o arquivo ser baixado corretamente
time.sleep(5)

# Recebe os arquivos do diretório na variavel
files = os.listdir(src)

# Verifica se possui algum arquivo com a extensão zip no diretório
MetadataFiles = pd.DataFrame([])
# Verifica se possui algum arquivo com a extensão zip no diretório
for file in files:
    if file.lower().endswith('.zip'):
        zip = os.path.join(src, file)
        print(zip)
        # Caso tenha o arquivo zip, cria um data frame para vermos os dados dentro do arquivo zip
        with zipfile.ZipFile(zip) as myzip:
            for info in myzip.infolist():                
                MetadataFiles = MetadataFiles.append(pd.DataFrame({'ZipFile': [os.path.basename(zip)],'FileName': [info.filename], 'Extension': [os.path.splitext(info.filename)[1].lower()], 'Size': [str(info.file_size/1000) + ' Kb'], 'Directory': [src],'Modified': [str(datetime.datetime(*info.date_time))]}))
                df = pd.DataFrame(MetadataFiles, columns = ['ZipFile','FileName','Extension','Size', 'Directory', 'Modified'])
                # Mostra os data frame criado dentro do aquivo zip
                print(df.head())

# Extrai somente os arquivos com a extensão TXT do arquivo zip na variavel do diretório de destino
QtdArq = 0
with zipfile.ZipFile(zip) as myzip:
    for FileName in myzip.namelist():
        if FileName.lower().endswith(".txt"):
            myzip.extract(FileName, src)
            QtdArq +=1

# Exibe uma mensagem que foi descompactado corretamente
print("Foram descompactados " + str(QtdArq) + " arquivos no diretório " + str(src))

# Renomeia o arquivo descompactado para o nome desejado, e salva no diretório de destino da variavel dst
os.rename(pathlib.Path(str(src) + "\\EMISSOR.TXT"), pathlib.Path(str(src) + "\\I_PI_EMISSOR.TXT"))
os.rename(pathlib.Path(str(src) + "\\NUMERACA.TXT"), pathlib.Path(str(src) + "\\I_PI_NUMERACA.TXT"))

# Enquanto os arquivos não estiverem no diretório extraídos, ele aguarda 1 segundo
while not glob.glob(str(src) + "\*.TXT"):
    time.sleep(1)
else:
    # Copia os arquivos extraidos o para o diretório da variavel dst
    QtdArq = 0
    for file in files:
        if os.path.isfile(os.path.join(src, file)):
            if file.lower().endswith('.txt'):
                shutil.copy(os.path.join(src, file), dst)
                QtdArq +=1
    # Exibe uma mensagem de quantos arquivos foram copiados
    print("Foram copiados " + str(QtdArq) + " arquivos, do diretório " + str(src) + " para o diretório " + str(dst))


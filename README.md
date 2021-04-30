# Obtendo os dados da B3 utilizando Python e frameworks de RPA

A documentação deste repositório também pode ser localizado no artigo do meu perfil no [Medium](https://guimatheus92.medium.com/obtendo-os-dados-da-b3-utilizando-python-e-frameworks-de-rpa-13d65732a1ed "Medium").

------------

Para funcionar, você deve alterar o diretório onde os arquivos deverão ser baixados.
```python
# Define o nome do diretório onde está o arquivo baixado
src = pathlib.Path("D:\\Users\\F02579\\Downloads")
```

E define o diretório para onde os arquivos baixados serão copiados.
```python
# Define o diretório aonde o arquivo será copiado após baixado
dst = pathlib.Path("D:\\Users\\F02579\\Documents")
```

Para abrir o navegor do Google Chrome automaticamente, deverá definir o diretório aonde o driver do Chrome estará localizado.
```python
executable_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
```

O arquivo do Chrome Driver pode ser encontrado [aqui](https://chromedriver.chromium.org/downloads "aqui") :tw-1f4ce:.

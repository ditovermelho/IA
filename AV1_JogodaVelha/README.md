# Repositório da Primeira Avaliação de Inteligência Artificial
__Objetivos:__
### Atividade 1
__Heurística, ML com Jogo da Velha__

Faça uma implementação em Python do Jogo da velha, conforme explicação dada nos links abaixo.
1. Parte1: https://www.youtube.com/watch?v=AhO-KN_tXSM
2. Parte2: https://www.youtube.com/watch?v=F9_giZ6Qjs0
3. Parte3: https://www.youtube.com/watch?v=HliION59JRA
4. Parte4: https://www.youtube.com/watch?v=Ss4wAOmyVTg

Caso encontre dificuldade, siga nossa dica de código na .pythonfile/dica.py

### Atividade 2
__Contexto e Tema__

O jogo da velha é um típico jogo que pode ser facilmente caracterizado por matrizes. Por
exemplo, na Seção 3, inserimos uma matriz chamada “matrix”, cuja jogada do “X” possui valor -1
e jogada do “O” possui valor 1. Obviamente, a soma de uma linha, coluna, ou diagonal possui valor
mínimo -3 ou máximo 3, cujas ocorrências dão vitória respectivamente ao “X” ou “O”. Como
verificador de vitória, fizemos a soma de cada __linha, coluna, diagonal1 e diagonal2__, para checar
se houve ou não vitória de algum jogador envolvido. Para isso foi usada a ideia de multiplicação de
__matrizes 3x3__: com matriz __3x1__ ou __1x3__, diminuindo consideravelmente o código original
disponibilizado nos vídeos informados na __Atividade 1__. Contudo, a estratégia adotada pela __CPU__ é pouco
inteligente, por sortear aleatoriamente uma jogada no tabuleiro.

1. Pense em uma heurística para melhorar isso, colocando-a no papel e explicando
posteriormente sua ideia nas aulas de entrega;
2. Implemente sua estratégia, coloque para rodar no GoogleColab e anexe seu
código na data definida para entrega;
3. Tente usar Machine Learning (ML), conforme demonstramos em sala um
problema de classificação:
* Link: https://colab.research.google.com/drive/1YUYhCdl1r80rfj8z_1l6o93XnXVXHzWQ?usp=sharing
* Com ML, houve possibilidade? Falhou? Melhorou? Como/Qual foi sua experiência?

### Dica de código do jogo da velha, baseado nos vídeos disponibilizados, com algumas otimizações
Caso encontre dificuldade, siga nossa dica de código na .pythonfile/dica.py

## Comandos de inicio de projeto 
* Criando maquina virtual:
```javascript
python -m venv venv
```

* Atualização do pip da venv:
```javascript
python -m pip install --upgrade pip
```

## Comandos de geração de requerimentos do projeto
* Pipreqs:
```javascript
pip install pipreqs
```
Essa biblioteca permite criar o arquivo de requerimento do projeto, puxando apenas as dependências do projeto. A única dependência 
desse pacote e, que todos os arquivos estejam dentro de uma pasta. 

No nosso caso:
```javascript
pipreqs ./pythonfile
```
ou para forçar a criação:
```javascript
pipreqs --force ./pythonfile
```
O pipreqs ira ler todos os arquivos da pasta e identificara todos 
os pacotes necessários para o projeto. Assim, é preciso prestar atenção aos pacotes que não são invocados mas são necessários para o projeto, como o lxml para quem usa BeutifulSoup. fonte: https://medium.com/pyladiesbh/requirements-em-python-ec88b42058a6.

* Freeze:
```javascript
pip freeze > requirements.txt
```
O pacote freeze ira criar os requerimentos do projeto com base nas bibliotecas instaladas no ambiente.

* Instalação dos requerimentos:
```javascript
pip install -r requirements.txt
```
basta digitar o comando acima no CMD.
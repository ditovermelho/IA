# Repositório da Segunda Avaliação de Inteligência Artificial
### 1. Instruções:
#### 1.1 Links
1. Vídeo1: https://youtu.be/cNLPt02RwF0
2. Exercício1: https://drive.google.com/file/d/1eJJmCYNgbXjk-nc3NjDoIHnnED4ek7-l/view
3. Dados (emais.csv): https://drive.google.com/file/d/1hz9zl5EglCLy-oLZz-LDEv3JZKDAYYxM/view

#### 1.2 Contexto e Definições das Atividades 
1. A atividade avaliativa deve ser realizada em __equipe__ de no máximo __2 alunos__;
2. A __entrega__ dos __códigos__, __exercícios e/ou textos__ se dará em __DATA1=05/06/2023__;
3. A __apresentação__ de __resultados__ se dará também na __DATA1__. Quem estiver remotamente, gravar apresentação
de seus resultados e submeter link;
4. __Requisitos__: __atividade__ e __formas__ de __entrega__:
1. __[Pontos 1] Atividade 1__: Exercício que explicamos em nossas aulas, disponibilizando código conforme
__1.1 Links→ Exercício1__. O Código que se deve entregar, mais a parte final (sua solução
usando a coluna categórica), encontra-se no __Exercício1 (ver 1.1 Links)__. Você deve descompactar
e transcrever os códigos das imagens para o seu __notebook Colab__, anexando seu __notebook Colab__ na entrega do trabalho;
2. [Pontos 8] Atividade 2: Pesquisar, fundamentar e se possível implementar uma estratégia de
ML para filtro de Spam. Por exemplo você pode começar observando o que foi feito neste vídeo:
Vídeo1 (ver 1.1 Links). Após concluída sua pesquisa, apresentar o que foi feito até a DATA1.
Acadêmicos do remoto, anexar vídeo para referida apresentação;
3. __[Pontos 1]__ Entrega dentro do prazo.

#### 1.3 Avaliação
Somatório da pontuação individual dos requisitos, profundidade na solução e no tema abordado

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
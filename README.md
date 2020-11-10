# epidemiologicalDataRecords
Um sistema de cadastro de dados epidemiológicos para o projeto de Laboratório de Engenharia de Software no curso de Análise e Desenvolvimento de Sistemas da Fatec

**Link do vídeo no Youtube:** https://youtu.be/Q4tswKxIHg8

## Configuração e Instalação :computer:

Para se executar a aplicação localmente, tenha o **python3.6x** instalado e crie um _ambiente virtual_:

```sh
$ python3 -m venv nome_do_ambiente
```
Note que uma nova pasta foi criada na raiz do projeto com o nome que você deu. Agora ative o ambiente virtual:

```sh
$ source nome_do_ambiente/bin/activate
```

Em seu terminal deve estar sendo mostrada entre parênteses o nome da seu ambiente, isso significa que ele já está ativado
Em seguida, instale as dependencias necessárias no arquivo **requirements.txt**:

```sh
(nome_do_ambiente)>$ pip install -r requirements.txt
```

Antes de executarmos a aplicação, verifique seu banco de dados MySQL e no arquivo `config.py` altere o valor da variável `SQLALCHEMY_DATABASE_URI` para os dados do seu banco de dados MySQL da seguinte forma:


```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<usuario>:<senha>@localhost/<nome_do_banco>'
```

Agora rode os seguintes comandos para que sejam criadas as devidas tabelas no banco de dados:

```sh
(nome_do_ambiente)>$ python run.py db migrate
(nome_do_ambiente)>$ python run.py db upgrade
```

E finalize inicializanado a aplicação com:

```sh
(nome_do_ambiente)>$ python run.py runserver
```

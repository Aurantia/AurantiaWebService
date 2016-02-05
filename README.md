# Dillinger

A AurantiaWebService é uma API REST escrita em Python utilizando o microframework Flask. Ela é parte fundamental do projeto Aurantia, fornecendo dados dos arduinos para utilização e integração com outras aplicações.

## Utilização
Para utilizar o projeto, deve-se antes realizar algumas configurações no ambiente local do desenvolvedor para fazer com que o mesmo seja executado da forma correta. O primeiro passo é instalar os pacotes relacionados ao **POSTGRES**.
```sh
$ sudo apt-get install postgresql postgresql-contrib libpq-dev python-dev
```
Após instalarmos o POSTGRES na nossa máquina é necessário instalar dois pacotes do python, que serão utilizados para criar o ambiente virtual.
```sh
$ pip install virtualenv virtualenvwrapper
```
Além de fazer a instalação, ainda é preciso referenciar algumas variáveis para que os próximos comandos possam ser reconhecidos. Para tal, iremos adicionar após a última linha presente no arquivo **~/.bashrc** os seguintes comandos:
```sh
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```
Para terminar esta parte, vamos recarregar o arquivo **bashrc**.
```sh
source ~/.bashrc
```
Agora, precisamos criar um ambiente virtual para isolarmos as dependências do nosso projeto.
```sh
$ mkvirtualenv aurantia-webservice
```
Após criarmos o nosso ambiente virutal, devemos ir até a pasta onde está o nosso projeto clonado e executar o seguinte comando:
```sh
$ pip install -r requirements.txt
```
O comando acima fará com que todas as depedências necessárias para o projeto ser executado, sejam baixadas e instaladas.
O próximo passo é configurar o ambiente virtual, para ele adicionar as variáveis que o nosso projeto precisa para ser executado. Para tal, vamos editar o arquivo **postactivate**. Este arquivo fica no seguinte diretório: $VIRTUAL_ENV/bin/postactivate. Com o arquivo aberto, adicione as seguintes linhas:
```sh
export APP_SETTINGS="settings.DevelopmentConfig"
export DATABASE_URL="postgres://postgres:aurantiax@localhost/aurantiadb"
```
Na primeira linha definimos o tipo de configuração que queremos para quando o servidor local for executado(essa configuração está presente no arquivo **settings.py**). E na segunda linha definimos a url do banco de dados postgres.
Por fim, é preciso apenas executar o comando:
```sh
$ python manage.py runserver
```
Para testar, basta executar o seguinte comando:
```sh
$ curl -i http://127.0.0.1:8080/api/
```
O resultado será algo como:
```sh
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 48
Server: Werkzeug/0.11.3 Python/2.7.6
Date: Fri, 05 Feb 2016 20:02:13 GMT

{
  "aurantia": "project", 
  "hello": "world"
}
```

# Licença

This file is part of AurantiaWebService.

AurantiaWebService is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

AurantiaWebService is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with AurantiaWebService.  If not, see <http://www.gnu.org/licenses/>.
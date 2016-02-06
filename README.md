# AurantiaWebService

The Aurant WebService is a REST API written in Python using the microframework Flask. It is a fundamental part of Aurant project, providing data from Arduino to use and integration with other applications.

## Usage
After cloning the project and enter the directory, you must download and install all project dependencies. It is noteworthy that it is extremely important that you create a virtual environment (with virtualenv) to run the project. You must run the following command:
```sh
$ pip install -r requirements.txt
```
Also add an environment variable to set the local server configuration when it runs. To do this, you should go to the **postactivate** file(this file is located in $VIRTUAL_ENV/bin) and add the following line:
```sh
$ export APP_SETTINGS="settings.DevelopmentConfig"
```
Now that everything is ready, simply lift the server. Use the following command:
```sh
$ python manage.py runserver
```
The url of api is this: http://localhost:8080/api/.
# License

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
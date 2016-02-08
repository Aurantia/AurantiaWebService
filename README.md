# AurantiaWebService
[![Python version](https://img.shields.io/badge/python-v2.7-orange.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-GPL-blue.svg)](http://www.gnu.org/licenses/gpl-3.0.en.html)

The AurantiaWebService is a REST API written in Python using the microframework Flask. It is a fundamental part of Aurant project, providing data from Arduino to use and integration with other applications.

## Usage
After cloning the project and enter the directory, you must download and install all project dependencies. It is noteworthy that it is extremely important that you create a virtual environment (with virtualenv) to run the project. You must run the following command:
```sh
$ pip install -r requirements.txt
```
We will also add two variables. The first set the local server configuration, the second sets the url of the site database. To do this, you should go to the **postactivate** file(this file is located in $VIRTUAL_ENV/bin) and Add the following lines:
```sh
export APP_SETTINGS="settings.DevelopmentConfig"
export APP_TESTING="settings.TestingConfig"
export DATABASE_URL="your-database-url"
```
Finally, you must start the database and raise the local server. To start the database, run the following commands:
```sh
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```
Now that everything is ready, simply raise the server. Use the following command:
```sh
$ python manage.py runserver
```
The url of api is this: http://localhost:8080/api/.

## Database Model
![Database Model](https://i.imgsafe.org/715c1c9.jpg)
## Routes
**/api/**: Returns all arduino. **[GET]**

**/api/status/**: Returns all arduino status. **[GET]**

**/api/[arduino_id]/**: Returns all arduino data. **[GET]**

**/api/[arduino_id]/status/**: Return arduino status. **[GET]**

**/api/lab/[lab_id]/**: Returns all arduino lab. **[GET]**

**/api/lab/[lab_id]/status/**: Returns status of all arduino lab. **[GET]**

**/api/register-arduino/**: Register an arduino and returns an access token for this arduino. **[POST]**

**/api/arduino-signal/**: Register a set of data collected by a particular Arduino. Returns "success" if everything worked out, and "integrity data error" when the access token is wrong or the Arduino does not exist. **[POST]**
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

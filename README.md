# Garnet Flask API Boilerplate

Author: Pedro Guzmán (pedro@subvertic.com)

License: MIT

## Description

Garnet is a basic boilerplate Flask-based application that provides some
basic features out of the box that can be easily configured and extended. 
Some of the provided features are the following:


- **MVC Support:** Full support for Model-View-Controller pattern. *Note:* 
If you plan to create a full web application, we recommend implementing 
*Views* using a frontend framework like ReactJs or Angular.

- **MongoEngine:** to intreact with MongoDB

- **JSONP Support (JSON with Padding):** Enables support for cross-origin 
requests without the need of enabling CORS.

- **JSON Web Token (JWT) Support** Support for JWT as specified in RFC 7519. 
 JWT allows secure representation of claims between two parties. 
 
 

![alt text](https://img.shields.io/pypi/v/nine.svg "PyPi")
![alt text](https://img.shields.io/badge/garnet--api-ready-blue.svg "garnet")
![alt text](https://img.shields.io/badge/Flask-0.12.2-brightgreen.svg "garnet")
![alt text](https://img.shields.io/badge/MongoDB-3.4.5-green.svg "garnet")
![alt text](https://img.shields.io/badge/MVC-Ready-orange.svg "garnet")
![alt text](https://img.shields.io/badge/JWT-Ready-blue.svg "garnet")

---
## Prerequisites

- Python 3.6.1
- Pip 9.0.1
- MongoDB 3.4.5
- Virtualenv (optional)

## Installation



Clone the repository in your local system:

````shell
$ git clone https://github.com/OneTesseractInMultiverse/Garnet.git
````

Install dependencies:
````shell
$ cd Garnet
$ pip install -r requirements.txt
````

Configure settings in **config.py** and setup your parameters such as validity of the
JWT tokens, connection parameters for MongoDB and logging. 

Run the application:

````
$ python run.py
````

Verify the application is running in your browser by navigating to:

````
http://127.0.0.1:8080
````

## Using Garnet

### Register a new user





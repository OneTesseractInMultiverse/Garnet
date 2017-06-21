# Garnet Flask API Boilerplate

Author: Pedro Guzmán (pedro@subvertic.com)

License: MIT License

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

By default, Garnet provides a basic account controller that enables registration 
of users as well as performing some basic operations such as querying users, 
updating password and updating email. Garnet also provides an authentication
endpoint that validates client credentials and issues JSON Web Tokens that can 
then be used to authenticate requests against protected resources. 

### Register a new user

The default registration endpoint is: **POST:** */api/v1/account* which takes a
json payload like the following:

```javascript 1.8
{
  "name": "YourName",
  "last_name": "YourLastname",
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "SuperSecretPassword"
}
```

### Authenticating and getting a JWT Token

In order to get a JWT Token, the following endpoint must be used: **POST:** 
*/api/v1/auth* and it takes the following json payload:

```javascript 1.8
{
  "username": "your_username",
  "password": "SuperSecretPassword"
}
```
If the data provided is correct, then you should receive a JWT Token. The default duration
of the Token is one hour, but this can be configured in *config.py* by modifying the *JWT_EXPIRATION_DELTA*
property. Here is an example token response:

```javascript 1.8
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NzQ1MDQ1NzYsImlhdCI6MTQ5ODAyNDU3NiwibmJmIjoxNDk4MDI0NTc2LCJpZGVudGl0eSI6ImJhZjFjMjI4LTg4NTAtNGJiMi1hMjBjLTYyYTgzZTQxM2NmNyJ9.mfwtdJVkjBmTSrqBUY-gky_XaUacMC5sFoV-aWsiDvg"
}
```

Now if you want to make authenticated requests to an API resource, you only need to include the token in the
Authorization Header as the following example:

```html
Authorization JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NzQ1MDQ1NzYsImlhdCI6MTQ5ODAyNDU3NiwibmJmIjoxNDk4MDI0NTc2LCJpZGVudGl0eSI6ImJhZjFjMjI4LTg4NTAtNGJiMi1hMjBjLTYyYTgzZTQxM2NmNyJ9.mfwtdJVkjBmTSrqBUY-gky_XaUacMC5sFoV-aWsiDvg
```






<h1 align="center">Welcome to codeleap 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/viniciosbarretos/codeleap/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
  </a>
</p>

> This is a small Django project to demonstrate Django CRUD functionality. The main app is an API created using Django Rest Framework.

#### 🏠 [Live API](https://google.com)

## Requirements

[Docker Compose](https://docs.docker.com/compose/install/)


## Install

Codeleap is deployed using Docker Compose. Edit the script to configure the environment variables to fit your requirements.

```sh
# clone repository
git clone git@github.com:viniciosbarretos/codeleap.git

# change directory to repo
cd codeleap

# start the container using the docker-compose command
docker-compose up
```

## Usage

To access the application go to the URL defined at docker-compose.yml. The default URL is http://localhost:80/



## API Validators

* All usernames should start with @
* Once set, you can't change username
* You can't set/change object ID and creation datetime

## CORS Policy

By default, all cors requests are blocked, except from `https://dev.codeleap.co.uk/`.


## Run tests

```sh
docker-compose run app-django python manage.py test
```

## Author

👤 **Vinicios Barretos**

* Github: [@viniciosbarretos](https://github.com/viniciosbarretos)
* LinkedIn: [@vinicios-barretos](https://linkedin.com/in/vinicios-barretos)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/viniciosbarretos/codeleap/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2020 [Vinicios Barretos](https://github.com/viniciosbarretos).<br />
This project is [MIT] licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)

# codeleap

## Development Environment

### Requirements
```
Python >= 3.8
virtualenv
```

### Install
```
# create virtual environment
virtualenv env-codeleap

# enable virtualenv
source env-codeleap/bin/activate

# install app requirements
pip install -r requirements.txt
```

### Running the Application

Before running the application we need to create DB tables. Note that if you are running the application without Docker, the database used will be sqlite. You can change the database settings in the env.py file.
```
python manage.py makemigrations
python manage.py migrate
```

Now you can run the web server:
```
python manage.py runserver
```

To access the application go to the URL <http://localhost:8000/>


### Unit Tests
```
# enable virtualenv (if it is disabled)
source env-codeleap/bin/activate

# run tests
python manage.py test
```

### Logging
Advanced logging is saved on django.log file. Use your text editor to see it.
```
less django.log 
```

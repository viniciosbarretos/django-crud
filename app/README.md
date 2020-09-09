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

#### django-admin.exe startproject myproject .

#### python .\manage.py startapp home

#### Add a urls.py in home app folder
#### Add a template file in the project

#### install mysqlclient with pip

#### change 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'your_host',  # Typically 'localhost' or '127.0.0.1'
        'PORT': 'your_port',  # Typically '3306'
    }
} 
```

##### in settings file.
##### then :
```
python .\manage.py migrate  
python .\manage.py makemigrations
```
##### Add models in models file

##### Add "home.apps.HomeConfig" to INSTALLED_APPS
```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home.apps.HomeConfig"
]
```
##### Add "DIRS": [BASE_DIR/"templates"] to TEMPLATES in setting file

##### Create a templates folder in home

##### Use render in a function in views that show all students in show_list.html

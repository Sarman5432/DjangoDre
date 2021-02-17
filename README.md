# DjangoDre

## Personal Notes

`django-admin startproject djangoapi` 

`py -m venv env` //virtual environment

`source env/Scripts/activate` //start the ve

`pip install django djangorestframework django-cors-headers pillow` //install packages in the virtual machine

`py manage.py runserver` //run server

`py manage.py startapp fighters` //add fighters app

## Added to settings.py 
`import os` //get access to OS operations

`ALLOWED_HOSTS = ['*']` //no security so run on any ip address
`CORS_ORIGIN_ALLOW_ALL = True`

Media used to allow image input from user
```
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "/media/").replace("\\", "/")
```
`'corsheaders.middleware.CorsMiddleware'` //added to middleware

`'rest_framework'` //added to installed apps

`'fighters'` //added to installed apps


// NOTE: create new INSTALLED_APP for each app/api endpoint (ex. py manage.py startapp fighters)

## Added to models.py
`py manage.py makemigrations` //looks in models and "compiles" them to be able to migrate

`py manage.py migrate` //actually run the migrations to make the table in the database


## serializers.py 
This is where json and python are converted for api calls






















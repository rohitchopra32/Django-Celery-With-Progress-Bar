# Django-Celery-With-Progress-Bar
This is a simple example about integrating Celery in Django website, it uses celery to run a long task and shows a progress bar about the progress of the task.

# Dependecies

* Celery
* Django
* Redis

# How to run:

```
  git clone https://github.com/rohitchopra32/Django-Celery-With-Progress-Bar.git
  cd Django-Celery-With-Progress-Bar
  install dependencies from requirements.txt file
  restart redis server
  celery -A celery_try worker -l info
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```

Then visit [http://127.0.0.1:8000/index/](http://127.0.0.1:8000/index/).


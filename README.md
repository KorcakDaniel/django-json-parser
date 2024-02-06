# JSON parsing Django application

A JSON parsing API written in Python using Django MVC architecture based framework.

## Routes

- `import/` - `POST` endpoint which accepts a JSON formatted request body and parses it
- `detail/<modelname>/` - `GET` a list of entries based on the name of a model
- `detail/<modelname>/<id>` - `GET` details of the entry given

## Instructions

1. Create a virtual environment using `python3 -m venv env`
2. Run the environment
   - `path\to\env\Scripts\activate.bat` on Windows
   - `source /path/to/env/bin/activate` on Unix/MacOS
3. Install the dependencies `pip install -r requirements.txt`
4. Run this command to get your personal secret key
   - `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
5. Copy the key and save it as an environment variable following [this](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Environment_Variables.html) guide
6. Run the application inside the project directory `python3 manage.py runserver`
7. Now the application should be working

## Dependencies

- [Django](https://github.com/django/django)
- [Django REST framework](https://github.com/encode/django-rest-framework)

## License

Licensed under [MIT License](https://github.com/divine-within/json-parsing-django/blob/main/LICENSE)

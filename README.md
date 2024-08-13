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
6. To create the defined database schema, run `python3 manage.py migrate`
7. Run the application with the following `python3 manage.py runserver`

## Usage

1. Import data similar to the `data/test_data.json`, using the `/import` endpoint
2. Retreive the imported model, using `/detail/<modelname>` endpoint
3. Retreive the model data, using `/detail/<modelname>/<id>` endpoint

Disclaimer: The API works only with models specified below.

## Implemented models and their serializers

- Catalog
- Image
- Attribute
- AttributeName
- AttributeValue
- Product
- ProductImage
- ProductAttributes

## Dependencies

- [Django](https://github.com/django/django)
- [Django REST framework](https://github.com/encode/django-rest-framework)

## License

Licensed under [MIT License](https://github.com/divine-within/django-json-parser/blob/main/LICENSE)

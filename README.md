# BookCafe

Live Deme: [Link](http://a1364t.pythonanywhere.com/)

BookCafe is a full CRUD application made using Django, Postgresql, Docker, Bootstrap, and google book API. This app provide an environment for book lovers to find popular books, leave comments, and share the books they liked.

# Usag
Browing the website doesn't require user Sign in, however reading book detail, adding a new book, and leaving comments require user account creation or login.
When user add a new book, the description and cover image are optional fields. If user leave them blank, cover image and description will be added to the database from google book API.
If user is nor happy with the auto generated description or cover image, they can edit the book info. 
A user who created a book has only access to edit and delete button in book detail template.

# Quick Start

1- Set up the [Python Virtual Environmen] (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment)

2- Running the following commands (If you are on Windows, you may use ```py``` or ```py -3``` instead of ```python``` to start the Python)

# Buges/Issues
- Manually uploaded cover image doesn't work properly.
- Navbar doesn't work properly on small screens.

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser # Create a superuser
python manage.py runserver
```

3- open a browser and enter ```http://127.0.0.1:8000/admin ``` to open the admin panel. Enter the username and poassword of for super suser.

4- open a tab to ``` http://127.0.0.1:8000/``` to see the main site.


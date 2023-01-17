# BookCafe

Live Demo: [Link](http://a1364t.pythonanywhere.com/)

BookCafe is a full CRUD application made using Django, Postgresql, Docker, Bootstrap, and Google book API. This app provides an environment for book lovers to find popular books, leave comments, and share the books they like.

# Usage
Browsing the website doesn't require a user to Sign in, however reading book detail, adding a new book, and leaving comments require user account creation or log in. <br />
Users can add a new book, the description and cover image are optional fields in the book creation form. When the user creates a new book, the cover image and description of the book will be added to the database from Google book API. If the user leaves cover image or description blank, they will show on the page from Google API. <br />
If user is not happy with the auto-generated description or cover image, they can edit the book info. <br />
A user who created a book has only access to the edit and delete buttons in the book detail page. <br />

# Bugs/Issues
- Manually uploaded cover image doesn't work properly.
- Navbar doesn't work properly on small screens.


# Quick Start
1- Set up the [Python Virtual Environment] (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment)

1- Set up the [Python Virtual Environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment)

2- Running the following commands (If you are on Windows, you may use ```py``` or ```py -3``` instead of ```python``` to start the Python)

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser # Create a superuser
python manage.py runserver
```

3- open a browser and enter ```http://127.0.0.1:8000/admin ``` to open the admin panel. Enter the username and password of for superuser.

4- open a tab to ``` http://127.0.0.1:8000/``` to see the main site.


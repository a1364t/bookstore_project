# BookCafe

Live Demo: [Link](http://a1364t.pythonanywhere.com/)

**BookCafe** is a full-stack CRUD application built with Django, PostgreSQL, Docker, Bootstrap, and the Google Books API. It provides a platform for book lovers to share their favourite reads, explore popular books, and engage with others through comments.

## Features

- Browse and discover books without signing in.
- Create an account or log in to:
  - Share new books with the community.
  - Leave comments on books shared by others.
  - Edit or delete books you’ve added.
- Automatically fetch book details (description and cover image) from the Google Books API when adding a new book.
- Option to customise book details, including cover images and descriptions, if the auto-fetched data doesn't meet your expectations.
- Clean and responsive UI with Bootstrap integration.

## How It Works

### Browsing the Site

Anyone can browse the website to explore shared books and their details.

### User Actions

- **Add New Book**: When creating a book, the description and cover image fields are optional. If left blank, these details will be fetched automatically using the Google Books API.
- **Editing Book Info**: Users can modify book details, including replacing auto-fetched descriptions or cover images.
- **Access Control**: Only the creator of a book can edit or delete it.

### Comments

Users can comment on books shared by others to share thoughts or feedback.

## Quick Start

1- Set up the [Python Virtual Environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment)

2- Running the following commands

```bash
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser # Create a superuser
    python manage.py runserver
```

3- open a browser and enter `http://127.0.0.1:8000/admin ` to open the admin panel.
Log in with the superuser credentials you created.

4- open a tab to ` http://127.0.0.1:8000/` to access the main page.

## Password Reset

- BookCafe uses Gmail’s SMTP server to handle password reset functionality.
- If users forget their password, they can click on Forget password link, and an email will be sent using Gmail’s SMTP service to guide them through the process.

## Technologies Used

- **Backend**: Django
- **Frontend**: Bootstrap
- **Database**: PostgreSQL
- **API**: Google Books API
- **Containerisation**: Docker
- **Email Service for Password Reset**: Gmail SMTP

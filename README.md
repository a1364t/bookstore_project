# BookCafe

Live Deme: [Link](http://a1364t.pythonanywhere.com/)

BookCafe is a full CRUD application made using Django, Postgresql, Bootstrap, and google book API. This app provide an environment for book lovers to find popular books, leave comments, and share the books they liked.

# Usag
Browing the website doesn't require user Sign in, however reading book detail, adding a new book, and leaving comments require user account creation or login.
When user add a new book, the description and cover image are optional fields. If user leave them blank, cover image and description will be added to the database from google book API.
If user is nor happy with the auto generated description or cover image, they can edit the book info. 
A user who created a book has only access to edit and delete button in book detail template.



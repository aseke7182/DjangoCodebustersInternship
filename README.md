## Django Project 27.01.2020 for CodeBusters Internship

### How to start working:
- Download everything from requirements.txt 
        
        $ pip freeze -r requirements.txt
- go in project folder, and wirte:

        $ python manage.py makemigrations
        $ python manage.py migrate
        $ python manage.py runserver
     
   Now, you could work with this system.   
   
----


/admin/ -> to view admin page   

/signup/ -> create new User,methods: POST, should not be auth., 
body: {
	"username": CharField,
	"password": CharField,
	"email": CharField
}

/login/ -> login User, methods: POST, shouldn't be auth.,
body: {
    "username": CharField,
    "password": CharField
}

/logout/ -> logout User, methods: POST, must be auth. with Token in header, no body

/users/ -> show all registered users, methods: GET, shouldn't b auth, no body, in GET method retrieves list of Users

/reviews/ -> show all written reviews from all users, must be superuser, methods: GET, must be auth. with Token in header, no body, in GET method retrieves list of Reviews

/company/ -> show all companies or create new company, methods: GET, POST, shouldn't be auth., no body, in GET method retrieves list of Companies,

/company/<int:pk>/ -> get, update, delete Company with (pk) id, methods: GET, PUT, DELETE, shouldn't be auth., no body

/review/ -> create new review or get all reviews fromm loggined user, methods: GET, POST, must be auth. with Token in header, in GET method retrieves list of Reviews,
body: {
	"rating": IntegerField,
	"title":  CharField,
	"summary": CharField,
	"company": IntegerField
}

/review/<int:pk>/ -> get, delete Review with (pk) id iff this review written by loggined user, methods: GET, DELETE, must be auth. with Token in header, no body



Sorry for that horrible Documentation, haven't experienced before.

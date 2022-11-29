# django Porjects Managemaent App
This project was created with django framework which is built on python language
then we can access the site through http://127.0.0.1:5000.

>__when we are activating the venv__ we should run these commands to migrate the data to the database:

```
python manage.py makemigrations
```

then:

```
python manage.py migrate
```

 ### <mark style="background-color: whitesmoke;font-weight: bold; padding: 4px">5- creating an admin for the website</mark>
 <br/>

 >if we want to access the admin url through  __/admin__ end point then we should create it the admin by running this command:

 ```
python manage.py createsuperuser
```

then we can determine his information.

 ### <mark style="background-color: whitesmoke;font-weight: bold; padding: 4px">6- running the server</mark>
 <br/>

 > Finally, we can run the server like this:

 ```
 python manage.py runserver
 ```

 we can go to http://localhost:8000 to access the website, and access the admin panel by going to http://localhost:8000/admin.

 we can deactivate the venv by running this command:
 ```
 deactivate
 ```

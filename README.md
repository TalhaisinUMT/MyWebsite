# MyWebsite

MyWebsite Django Project

This is a Django based project called MyWebsite, which includes a blog application. The project demonstrates the basic setup and functionality of a Django app, following the recommended structure and best practices.

Features:

1. App Structure:
    A Django project named MyWebsite containing an app named blog.
    Modular URL configuration using Django's include function.

2. Database Models:
    A Post model in the blog app with the following fields:
      title: A CharField (max length 100) for the post title.
      content: A TextField for the post content.
      created_at: A DateTimeField that automatically stores the post's creation timestamp.
    Migrations are applied to reflect the model in the database.

3. Templates:
    A post_list.html template to render a list of blog posts with the following:
      Display of post titles and their creation timestamps.
      Looping through posts using Django's template language.

4. Static Files:
    A static directory with a style.css file for basic styling, including:
      Customized font size and color for post titles.
      Spacing between posts for better readability.



Project Structure:

MyWebsite/

├── blog/

│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       └── post_list.html
│   ├── static/
│   │   └── blog/
│   │       └── style.css
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py

├── MyWebsite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py

├── manage.py




Setup Instructions:

1. Clone the repository:
   git clone <repository_url>
   
   cd MyWebsite
   

2. Create and activate a virtual environment:
   python m venv env
   
   source env/bin/activate   For Linux/Mac
   
   env\Scripts\activate      For Windows
   

4. Install dependencies:
   pip install r requirements.txt
   

6. Apply migrations:
   python manage.py makemigrations
   
   python manage.py migrate
   

8. Run the development server:
   python manage.py runserver
   

9. Access the application:
   Open a browser and visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)



 How It Works:

 Homepage: Displays a list of blog posts with their titles and creation timestamps.
 
 Admin Panel: Manage posts and other app features at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).



 Technologies Used:

 Backend Framework: Django
 
 Database: SQLite (default Django database)
 
 Frontend: HTML, CSS (basic styling)
 
 Version Control: Git & GitHub


Feel free to contribute or raise issues for improvements! 😊


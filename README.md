# Django Project
Django is a free and open-source web framework written in Python. It is designed to help developers take applications from concept to completion as quickly as possible. Django follows the model-template-view (MVT) architectural pattern. This means that it has three main components:
1. **Models**: These are classes that define the structure of the data stored in your Django application. A model is a Python class that subclasses django.db.models.Model. It defines the fields of the object and the data type of each field.
2. **Templates**: These are HTML files that define the structure of the user interface. They contain placeholders for dynamic content, which is filled in by the view.
3. **Views**: These are Python functions that handle requests from the user and return a response. A view is a Python function that takes a request and returns a response. It queries the models for the data needed to render the template, and then passes the data to the template to generate the final HTML response.

In Django, the request-response cycle works as follows:
1.  The user sends a request to the server.
2.  The Django web server receives the request and routes it to the appropriate view function.
3.  The view function queries the models for the necessary data and renders the template with the data.
4.  The rendered template is sent back to the user as a response.

# Django MVT Architecture

![MVT-Architecture](https://user-images.githubusercontent.com/103352460/210198146-f11bdd77-9ef0-4be9-84f7-a3ac0c26ff90.png)


To get started with a Django project, you'll need to install Django and set up a new project. Here are the steps you can follow:

1. Install Django:
```
pip install Django
```
2. Create a new Django project:
```
django-admin startproject myproject
```
This will create a new directory called "myproject" with the basic files and directories needed for a Django project.

3. Change into the project directory:
```
cd myproject
```

4. Run the development server:
```
python manage.py runserver
```
This will start the development server at http://127.0.0.1:8000/. You can visit this URL in your web browser to view your Django project.

To create a new app within your project, use the following command:

```
python manage.py startapp myapp
```

This will create a new directory called "myapp" with the basic files and directories needed for a Django app.

In Django, an "app" is a self-contained module that contains all the code and resources for a specific feature or functionality. A Django project can contain multiple apps, and each app can be used in multiple projects.

Some examples of common apps in a Django project are:

* A blog app that allows users to create and publish blog posts.
* A forum app that allows users to participate in online discussions.
* A shopping cart app that allows users to purchase products online.

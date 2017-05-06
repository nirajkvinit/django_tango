> # Chapter 3

## Basic Workflows
What you’ve just learnt in this chapter can be succinctly summarised into a list of actions. Here, we provide these lists for the two distinct tasks you have performed. You can use this section for a quick reference if you need to remind yourself about particular actions later on.
### Creating a new Django Project
1. To create the project run, ```python django-admin.py startproject <name>```, where <name> is the name of the project you wish to create.
### Creating a new Django application
1. To create a new application, run ```$ python manage.py startapp <appname>```, where <appname> is the name of the application you wish to create.
2. Tell your Django project about the new application by adding it to the ```INSTALLED_APPS``` tuple in your project’s ```settings.py``` file.
3. In your project ```urls.py``` file, add a mapping to the application.
4. In your application’s directory, create a ```urls.py``` file to direct incoming URL strings to views.
5. In your application’s ```view.py```, create the required views ensuring that they return a HttpResponse object.

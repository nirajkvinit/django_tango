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

## Exercises
Now that you have got Django and your new app up and running, give the following exercises a go to reinforce what you’ve learnt. Getting to this stage is a significant landmark in working with Django. Creating views and mapping URLs to views is the first step towards developing more complex and usable Web applications.
• Revise the procedure and make sure you follow how the URLs are mapped to views.
• Create a new view method called about which returns the following HttpResponse: 'Rango says here is the about page.'
• Map this view to /rango/about/. For this step, you’ll only need to edit the urls.py of the Rango application. Remember the /rango/ part is handled by the projects urls.py.
• Revise the HttpResponse in the index view to include a link to the about page.
• In the HttpResponse in the about view include a link back to the main page.
• Now that you have started the book, follow us on Twitter @tangowithdjango, and let us know how you are getting on!

## Hints
If you’re struggling to get the exercises done, the following hints will hopefully provide you with some inspiration on how to progress.
• In your ```views.py```, create a function called: ```def about(request):```, and have the function return a ```HttpResponse()```, insert your HTML inside this response.
• The regular expression to match ```about/``` is ```r'^about/'``` - so in ```rango/urls.py``` add in a new mapping to the ```about()``` view.
• Update your ```index()``` view to include a link to the about view. Keep it simple for now - something like Rango says hey there partner! ```<br/> <a href='/rango/about/'>About</a>```.
• Also add the HTML to link back to the index page is into your response from the ```about()``` view ```<a href="/rango/">Index</a>```.
• If you haven’t done so already, now’s a good time to head off and complete part one of the official Django Tutorial.

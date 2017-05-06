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

* Revise the procedure and make sure you follow how the URLs are mapped to views.
* Create a new view method called ```about``` which returns the following HttpResponse: ```'Rango says here is the about page.'```
* Map this view to ```/rango/about/```. For this step, you’ll only need to edit the ```urls.py``` of the Rango application. Remember the ```/rango/``` part is handled by the projects ```urls.py```.
* Revise the HttpResponse in the index view to include a link to the about page.
* In the HttpResponse in the about view include a link back to the main page.

## Hints
If you’re struggling to get the exercises done, the following hints will hopefully provide you with some inspiration on how to progress.

* In your ```views.py```, create a function called: ```def about(request):```, and have the function return a ```HttpResponse()```, insert your HTML inside this response.
* The regular expression to match ```about/``` is ```r'^about/'``` - so in ```rango/urls.py``` add in a new mapping to the ```about()``` view.
* Update your ```index()``` view to include a link to the about view. Keep it simple for now - something like Rango says hey there partner! ```<br/> <a href='/rango/about/'>About</a>```.
* Also add the HTML to link back to the index page is into your response from the ```about()``` view ```<a href="/rango/">Index</a>```.
* If you haven’t done so already, now’s a good time to head off and complete part one of the official Django Tutorial.


> # Chapter 4

## Basic Workflows
With the chapter complete, you should now know how to setup and create templates, use templates within your views, setup and use the Django development server to serve static media files, and include images within your templates. We’ve covered quite a lot!
Creating a template and integrating it within a Django view is a key concept for you to understand. It takes several steps, but will become second nature to you after a few attempts.
1. First, create the template you wish to use and save it within the templates directory you specified in your project’s ```settings.py``` module. You may wish to use Django template variables (e.g. ```{{ variable_name }})``` or template tags within your template. You’ll be able to replace these with whatever you like within the corresponding view.
2. Find or create a new view within an application’s ```views.py``` file.
3. Add your view specific logic (if you have any) to the view. For example, this may involve extracting data from a database and storing it within a list.
4. Within the view, construct a dictionary object which you can pass to the template engine as part of the template’s context.
5. Make use of the ```render()``` helper function to generate the rendered response. Ensure you reference the request, then the template file, followed by the context dictionary.
6. If you haven’t already done so, map the view to a URL by modifying your project’s ```urls.py``` file and the application specific ```urls.py``` file if you have one.

The steps involved for getting a static media file onto one of your pages are part of another important process that you should be familiar with. Check out the steps below on how to do this.
1. Take the static media file you wish to use and place it within your project’s static directory. This is the directory you specify in your project’s ```STATICFILES_DIRS``` list within ```settings.py```.
2. Add a reference to the static media file to a template. For example, an image would be inserted into an HTML page through the use of the ```<img />``` tag.
3. Remember to use the ```{% load staticfiles %}``` and ```{% static "<filename>" %}``` commands within the template to access the static files. Replace ```<filename>``` with the path to the image or resource you wish to reference. Whenever you wish to refer to a static file, use the static template tag!

The steps for serving media files are similar to those for serving static media.
1. Place a file within your project’s media directory. The media directory is specified by your project’s ```MEDIA_ROOT``` variable.
2. Link to the media file in a template through the use of the ```{{ MEDIA_URL }}``` context variable. For example, referencing an uploaded image cat.jpg would have an ```<img />``` tag like ```<img src="{{ MEDIA_URL}}cat.jpg">```.

## Exercises
Give the following exercises a go to reinforce what you’ve learnt from this chapter.
* Convert the about page to use a template as well, using a template called ```about.html```.
* Within the new ```about.html``` template, add a picture stored within your project’s
static files.
* On the about page, include a line that says, This tutorial has been put together by <your-name>.
* In your Django project directory, create a new directory called media, download a
picture of a cat and save it the media directory in a file called, cat.jpg.
* In your about page, add in the ```<img>``` tag to display the picture of the cat, to ensure that your media is being served correctly.


> # Chapter 5

## Workflow: Model Setup

Now that we’ve covered the core principles of dealing with Django’s ORM, now is a good time to summarise the processes involved in setting everything up. We’ve split the core tasks into separate sections for you. Check this section out when you need to quickly refresh your mind of the different steps.

### Setting up your Database
With a new Django project, you should first tell Django about the database you intend to use (i.e. configure DATABASES in ```settings.py```). You can also register any models in the ```admin.py``` module of your app to make them accessible via the admin interface.

### Adding a Model
The workflow for adding models can be broken down into five steps.
1. First, create your new model(s) in your Django application’s ```models.py``` file.
2. Update ```admin.py``` to include and register your new model(s).
3. Perform the migration ```$ python manage.py makemigrations <app_name>```.
4. Apply the changes ```$ python manage.py migrate```. This will create the necessary infrastructure within the database for your new model(s).
5. Create/edit your population script for your new model(s).

Invariably, there will be times when you will have to delete your database. When this happens, run the following commands from the ```manage.py``` module.
1. migrate your database - this will set everything up in the new database. Ensure that your app is listed in the migrations that are committed. If it is not, run the ```makemigrations <app_name>``` command, where ```<app_name>``` is the name of your app.
2. Create a new administrative account with the createsuperuser command.

### Exercises
Now that you’ve completed this chapter, try out these exercises to reinforce and practice
what you have learnt. Once again, note that the following chapters will have expected you to have completed these exercises!
* Update the Category model to include the additional attributes views and likes where the default values for each are both zero (0).
* Make the migrations for your app and then migrate your database to commit the
changes.
* Update your population script so that the Python category has 128 views and 64 likes, the Django category has 64 views and 32 likes, and the Other Frameworks category has 32 views and 16 likes.
* Delete and recreate your database, populating it with your updated population
script.
* Complete parts two and seven of the official Django tutorial. These sections will
reinforce what you’ve learnt on handling databases in Django, and show you additional techniques to customising the Django admin interface.
* Customise the admin interface. Change it in such a way so that when you view the
Page model, the table displays the category, the name of the page and the url


### Exercise Hints
If you require some help or inspiration to complete these exercises done, here are some hints.
* Modify the Category model by adding in the fields, view and likes as ```IntegerFields```.
* Modify the ```add_cat``` function in the ```populate.py``` script, to take the views
and likes. Once you get the Category ```c```, then you can update the number of views with ```c.views```, and similarly with likes. Don’t forget to ```save()``` the
instance!
* To customise the admin interface, you will need to edit ```rango/admin.py``` and create a ```PageAdmin``` class that inherits from ```admin.ModelAdmin```.
* Within your new ```PageAdmin``` class, add ```list_display = ('title', 'category', 'url')```.
* Finally, register the ```PageAdmin``` class with Django’s admin interface. You should
modify the line ```admin.site.register(Page)```. Change it to ```admin.site.register(Page, PageAdmin)``` in Rango’s ```admin.py``` file.

### Tests
To run the tests, issue the following command in the terminal or Command Prompt.
```$ python manage.py test rango```

# Building a Django App

## Create a django project.
The project will hold all the related apps for a software package. 

    django-admin startproject projectname   # projectname is the name of the django 'project'

This will create the directory structure:

    projectname/           # root directory, name doesn't matter to python
        manage.py          # command and control script
        projectname/            # this will be the python package 
            __init__.py    # marker for python, this is a package
            settings.py    # settings file sensitive, e.g. database passwords, should not be accessible
            urls.py        # the table of contents for the site
            wsgi.py        #  An entry-point for WSGI-compatible web servers to serve your project

Before you go farther, you will have to make it accessible outside the default 127.0.0.1:8000, so go to `projectname/settings.py` and alter it so that ALLOWED_HOSTS = ['*'].  Then make sure it works:

    python manage.py runserver # default server and port is 127.0.0.1:8000, use 0:8000 on Codenvy for testing

## Create an app inside the project
Each database is an individual app in the Django paradigm. 

    python manage.py startapp appname     # appname is thename of the database 'app'

This will create the directory structure, inside the `projectname` directory:

    appname/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py


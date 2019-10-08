from builder import dbproject


path = "/projects/environment/home/django-builder/OUTPUT"
name = "mysite"
project = dbproject(name, path)
project.build()

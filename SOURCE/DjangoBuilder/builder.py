import TEMPLATES
from base import dbbase
import os


class dbproject(dbbase):

    path = ""
    name = ""

    def __init__(self, name, path):
        super().__init__
        self.name = name
        self.path = path
        print("the name is %s" % self.name)
        print("the path is %s" % self.path)

    def build(self):
        self.create_project_directory()
        self.create_manage_py_file()
        self.create_project_subdirectory()
        self.create_init_py_file()
        self.create_settings_py_file()
        self.create_urls_py_file()

    def create_project_directory(self):
        os.mkdir(self.root_path())

    def create_project_subdirectory(self):
        os.mkdir(self.root_path() + "/" + self.name)

    def create_manage_py_file(self):
        content = TEMPLATES.manage_py.format(self.name)
        file = open(self.root_path() + "/manage.py", "w+")
        file.write(content)
        file.close()

    def create_init_py_file(self):
        file = open(self.project_path() + "/__init__.py", "w+")
        file.write("")  # __init__.py is empty
        file.close()

    def create_urls_py_file(self):
        file = open(self.project_path() + "/urls.py", "w+")
        file.write("nothing goes here")
        file.close()

    def create_settings_py_file(self):
        content = self.name.join(TEMPLATES.settings_py.split('{name}'))
        file = open(self.project_path() + "/settings.py", "w+")
        file.write(content)
        file.close()

    def root_path(self):
        return self.path + "/" + self.name

    def project_path(self):
        return self.root_path() + "/" + self.name

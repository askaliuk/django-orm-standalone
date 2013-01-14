Django ORM standalone example
=============================

Problem
-------
In one of my projects, i had architecture challenge to separate out Django ORM based data access layer and make it accessible for other components (django sites, third-party scripts, etc.). This project provides an example of solution.

Structure
---------
The application contains 3 main modules:
 - **data** - provides standalone data access module, based on Django ORM. It contains models and database settings.
 - **mysite** - simple Django site, which uses "data" module for data access purpose. It re-uses models from "data" module
   and can contain it's own specific models. It based on database settings from "data" module.
 - **test** - plain Python test, which has "data" module as dependency for data access purpose

Approach
--------
Proposed project structure requires "data" module to be importable and visible by other components. I don't like python path manipulations inside code, because it decreases portability. Also i would like to avoid have root package, which contain all components and use root import like "import root.data". My idea is to keep all components separated and use simple import like "import data". This task is could be accomplished by environment setup. That's why i'm using virtualenv and virtualenvwrapper.

How to use
----------
::

    cd django-orm-standalone
    pip install virtualenvwrapper
    mkvirtualenv django-orm-standalone
    add2virtualenv .
    pip install -r requirements.txt
    python data/manage.py syncdb
    python test/test_model_access.py

Django ORM standalone example
=============================

Problem
-------
Recently, I faced an architecture challenge: **how to separate the Django Models (ORM) from the rest of a web project and use them with other tools**. For example, reuse the web-site models in a command-line tool. This project is an example of such solution.

Structure
---------
The application contains 3 main modules:

* **data** - a standalone data access module, based on Django ORM. It contains the Models and Database Settings.
* **mysite** - a simple Django site, which uses the "data" module instead of redefining models once more. However, it can contain its own models which do not need to be shared. Also, "mysite" exports the Database Settings from the "data" module.
* **test** - a unitest, which also exports the "data" module.

Approach
--------
The proposed project structure enables us to import the "data" module by any other component. I avoid Python path manipulations inside the code, since this kills its portability and makes you to remember the paths. Also I prefer to to avoid having a root package, which would contain all components to rely on a root import like "import root.data". My idea is to keep all components separated and use a simple import like "import data". This task could be accomplished by a simple setup of the environment. For that, I rely on **virtualenv** and **virtualenvwrapper**.

How to use
----------
::

    # Install global modules and plug useful short-cuts into your Bash, reload it
    sudo pip install virtualenv
    sudo pip install virtualenvwrapper
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
    source ~/.bashrc

    # Create the virtual environment and install dependencies
    cd django-orm-standalone
    mkvirtualenv django-orm-standalone
    add2virtualenv .
    pip install -r requirements.txt

    # Create DB and run tests - a sample third-side component
    python data/manage.py syncdb
    python test/test_model_access.py

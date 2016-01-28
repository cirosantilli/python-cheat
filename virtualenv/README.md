# Virtualenv

Allows you to run programs in a controlled Python environment:

- python interpreter version
- version of each installed python module

It is therefore a virtualization method for Python aspects of the program, and helps ensure that every developer of a project runs the same environment.

`pip` is unlike most other more modern languages which have two separate utilities:

- an interpreter virtualizer (RVM, NVM)
- a package manager capable of doing local packages (Bundler, NPM)

virtualenv does not seem to install Python: it only uses what you specify: <http://stackoverflow.com/questions/11889932/specify-python-version-for-virtualenv-in-requirements-txt> which should be a `pythonX.Y` executable in your path.

Install virtualenv with pip:

    sudo pip install --upgrade virtualenv

The typical usage for virtualenv is to create a new one inside the project you are working on:

    cd python-project

Create a new environment that will use the `python2.7` interpreter:

    virtualenv -p python2.7 --distribute venv2.7

`--distribute` is recommended as this flags tells Virtualenv to use `distribute` instead of `setuptools` which is better as of 2013.

If `-p` is not given, the version used to run `virtualenv` is used instead.

Create a new environment that will use the `python3.3` interpreter:

    virtualenv -p python3.3 --distribute venv3.3

To activate the 2.7 environment we must source:

    . venv2.7/bin/activate

This has the following effects:

-   `pip` now refers to a local `pip` of the environment under `venv2.7`, as can be seen by:

        readlink -f "$(which pip)"

    `pip install` only installs packages locally to this environment.

-   `python` now refers to TODO what? The symlink chain ends in a python under `venv2.7`. Where did that interpreter come from?

-   `PS1` was changed, so that every shell lines starts with:

        (venv2.7)~/path/to/myproject
        user@host

Note how this is not like `git`: if we change directory we are still in the virtual environment, because we actually sourced something into our current shell.

When you want to exit do:

    deactivate

This has been defined by the activate source command and undoes it. But don't do that yet.

Check out that our Python version really is the one we wanted:

    python --version

Check out all the distribute installed programs:

    pip freeze

There should be very few in the list, much less than all of those we have previously installed. This means that we have a very clean environment for our new project to run on! Amongst the few present, `distribute` should be there since we will be using it to install the other dependencies.

Install a `termcolor` version `1.0.0` on it:

    pip install termcolor==1.0.0

Open up `venv2.7` and find the `termcolor` installed in there.
It is all local on our super clean environment.

Check our python version and `termcolor` version by running a script:

    python main.py

Now lets switch to the other env, but this time we install `termcolor` 1.1.0:

    . venv3.3/bin/activate
    pip install termcolor==1.1.0

And just like magic, if we run the same `python main.py` we see that the python version and `termcolor` versions both changed! How cool is that?!

Do open up `venv3.3` just to see that everything is in there once again: python interpreter and installed packages.

Once you've have enough fun, just do:

    deactivate

And we are back to the normal world.

## git and virtualenv

You should gitignore the local environment: <http://stackoverflow.com/questions/6590688/is-it-bad-to-have-my-virtualenv-directory-inside-my-git-repository>

Use `pip freeze` to get the packages I need into a `requirements.txt` and track that instead.

TODO: how to automatically specify which Python version is to be used? Like `.rvm` file for Ruby?

## Bibliography

- <http://simononsoftware.com/virtualenv-tutorial/>
- <http://stackoverflow.com/questions/2812471/is-there-a-python-equivalent-of-rubys-rvm>

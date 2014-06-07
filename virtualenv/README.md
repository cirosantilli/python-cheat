Allows you to run programs in an environment where Python aspects are controlled
This includes the possibility to control:

- python interpreter version
- version of each installed python module

This allows to control environments so that program behavior is reproducible.
This is fundamental for example for PaaS services, where you want to be sure
that your local tests reflect what happens on the server.

virtualenv can only control Python aspects. If you need even more control over the system,
the only way is to use a fully blown virtual machine like VirtualBox.
virtualenv is faster and more convenient if you only need to control Python characteristics.

Install virtualenv with pip:

    sudo pip install --upgrade virtualenv

The typical usage for virtualenv is to create a new one inside the project you are working on:

    cd python-project

Create a new environment that will use the `python2.7` interpreter:

    virtualenv -p python2.7 --distribute venv2.7

`--distribute` is recommended as this flags tells virtualenv to use
`distribute` instead of `setuptools` which is better as of 2013.

If `-p` is not given, the version used to run `virtualenv` is used instead.

The executable `python2.7` must be in your path.

This will create a directory named `venv2.7` and will put all everything
in there including the python interpreter binary we will be using,
and modules installed via `pip`. Take your time to look into that directory
and see how it is all there!

Create a new environment that will use the `python3.3` interpreter:

    virtualenv -p python3.3 --distribute venv2.7

To activate the 2.7 environment we must source:

    . venv2.7/bin/activate

This should change our `PS1` variable a little to indicate that we are now in the venv
to something like:

    (venv2.7)~/python
    ciro@ciro

Note how this is not like `git`: if we change directory we are still in the venv,
because we actually sourced something into our current shell

    cd ..
    cd -

When you want to exit do:

    deactivate

This has been defined by the source command and undoes it.
But don't do that yet.

Check out that our Python version really is the one we wanted:

    python --version

Check out all the distribute installed programs:

    pip freeze

There should be very few in the list, much less than all of those we have previously installed.
This means that we have a very clean environment for our new project to run on!
Amongst the few present, `distribute` should be there since we will be using it to install the other
dependencies.

Install a `termcolor` version `1.0.0` on it:

    pip install termcolor==1.0.0

Open up `venv2.7` and find the termcolor installed in there.
It is all local on our super clean environment.

Check our python version and termcolor version by running a script:

    python main.py

Now lets switch to the other env, but this time we install termcolor 1.1.0:

    . venv3.3/bin/activate
    pip install termcolor==1.1.0

And just like magic, if we run the same `python main.py` we see that the python version
and termcolor versions both changed! How cool is that?!

Do open up `venv3.3` just to see that everything is in there once again:
python interpreter and installed packages.

Once you've have enough fun, just do:

    deactivate

And we are back to the normal world.

# sources

- <http://simononsoftware.com/virtualenv-tutorial/>

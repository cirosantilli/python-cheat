# Getting started

On Ubuntu 12.04 install all dependencies with:

	./install-ubuntu.sh

On other systems, install Python-only dependencies with:

	sudo pip install -r requirements.txt

This does not include certain dependencies which may not be installable with `pip` such as SciPy build dependencies.

## Instal Python

Use `virtualenv` as early as possible. It's like Ruby `rvm` for Python, and allows you to have multiple installations at once.

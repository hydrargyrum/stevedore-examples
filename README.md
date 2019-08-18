# Examples to make Python plugins using `stevedore` and standard `setuptools`

`setuptools` is the widespread base library to install Python packages.
It comes with a lot of features, among which a very generic plugin system called "entry points".

Unlike most Python plugin systems, this one is builtin and very well supported.
It's also well integrated in the Python setup system, which allows plugins to be distributable with pip easily (with `setup.py`/`setup.cfg`) and deals correctly with virtualenvs.
And it covers most plugin use cases a project could have.

`stevedore` proposes an API on top of `setuptools`' API for simpler use.

This project contains very basic examples of how to use some of the patterns.

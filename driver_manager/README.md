# Drivers

Drivers are designed to provide the same sort of functionality but implemented differently or on a different backend, but only one driver will be chosen by the app.
For example, database drivers for having an app working on SQLite or on MySQL, or an output format.

https://docs.openstack.org/stevedore/latest/user/patterns_loading.html#drivers-single-name-single-entry-point

# Run example

Install:

    pip install ./src_mgr ./src_a ./src_b

Run:

    # Implemented by a plugin
    test-driver plain

    # Implemented by another plugin
    test-driver json

    # Error: not implemented by any plugin
    test-driver xml

The example app simply prints the "Hello world!" string in the desired format, but it doesn't contain any format builtin.
Formats are driver-type plugins. The command-line argument chooses the driver to load, and it's used to process the data.
A plugin shoud implement a function that formats a given string.

The example contains 2 plugins:

* "plain" formatter, which returns the string untouched
* "json" formatter, which converts the string to JSON format

# A plugin

For plugins to be linked to our app, they must be under the same "plugin namespace", which is merely an identifier shared in our app.
This plugin namespace is independant of Python's package namespace.

We will choose "plugin_test_driver" as our namespace.

The "json" plugin source is organized like this:

    src_a
    ├── setup.cfg
    ├── setup.py
    └── test_driver_json
        └── __init__.py

It could be in its own git repository!

The plugin code is in `test_driver_json/__init__.py` and is straightforward:

    import json
    def format(s):
        return json.dumps(s)

If we stopped now, the plugin could be installed with `pip` but it would only be usable by doing

    import test_driver_json
    test_driver_json.format('Hello world!')

This is because we didn't expose the plugin yet, but it's easy to do.

`setup.cfg` simply advertises the plugin:

    [options.entry_points]
    plugin_test_driver =
        json = test_driver_json:format

This syntax roughly says:

> Under the `plugin_test_driver` plugin namespace, we add an entry point named `json`
> and whose value is the function `format` in `test_driver_json` (or `test_driver_json.__init__`)

Note that we didn't refer to `stevedore` at all when building this plugin, only `setuptools`.

# The other plugin

The source folder tree is organized similarly:

    src_b
    ├── setup.cfg
    ├── setup.py
    └── test_driver_plain
        └── __init__.py

The "plain" plugin formatter is even simpler:

    def format(s):
        return s

And the `setup.cfg` advertises the `plain` key, and the `test_driver_plain` value:

    [options.entry_points]
    plugin_test_driver =
        plain = test_driver_plain:format

# App

Let's import basic things, and fetch driver name arg:

    import sys
    import stevedore.driver
    driver_name = sys.argv[1]

Use `stevedore` to load the chosen plugin, under our namespace, nothing much:

    em = stevedore.driver.DriverManager('plugin_test_driver', driver_name)

Then, run the plugin with the chosen input:

    def format_and_print(extension, s):
        # extension is the stevedore driver handler
        # extension.plugin is the advertised object
        print(extension.plugin(s))

    em.map(format_and_print, 'Hello world!')

`em.map` will use a callback with the chosen driver and the given input.

Our callback will receive the concrete driver instance, of the `stevedore.extension.Extension` class.
We can retrieve some metadata through it but don't care.

`extension.plugin` points to the value given is `setup.cfg`.
For example, in the "json" plugin, we have `json = test_driver_json:format`.
So, if `driver_name == "json"`, `extension.plugin` will point to the `format` function of the `test_driver_json` module.

We could directly call

    def format_and_print(extension):
        print(extension.plugin('Hello world!'))

    em.map(format_and_print)

But we can do even better, and pass the input as a dedicated argument

    def format_and_print(extension, s):
        print(extension.plugin(s))
        
    em.map(format_and_print, 'Hello world!')

`em.map()` takes as many arguments as the callback can take.

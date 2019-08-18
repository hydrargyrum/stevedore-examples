# Drivers

Drivers are designed to provide the same sort of functionality but implemented differently or on a different backend, but only one driver will be chosen by the app.
For example, database drivers for having an app working on SQLite or on MySQL, or an output format.

https://docs.openstack.org/stevedore/latest/user/patterns_loading.html#drivers-single-name-single-entry-point

# Run example

Install:

    pip install src_mgr src_a src_b

Run:

    # Implemented by a plugin
    test-driver plain

    # Implemented by another plugin
    test-driver json

    # Error: not implemented by any plugin
    test-driver xml

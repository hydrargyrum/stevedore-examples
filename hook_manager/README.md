# Hooks

Hooks are designed to let plugins attach themselves to something that will be broadcast to them and other plugins, for example, events.

https://docs.openstack.org/stevedore/latest/user/patterns_loading.html#hooks-single-name-many-entry-points

# Run example

Install:

    pip install src_mgr src_a src_b

Run:

    # Implemented by 2 plugins
    test-hook hook_1

    # Implemented by 1 plugin only
    test-hook hook_2

    # Implemented by 1 plugin only
    test-hook hook_3

    # Error: not implemented by any plugin
    test-hook hook_4

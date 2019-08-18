#!/usr/bin/env python3

import sys

import stevedore.hook


def main():
    try:
        hook_name = sys.argv[1]
    except IndexError:
        hook_name = 'hook_1'

    em = stevedore.hook.HookManager('plugin_test_hook', hook_name)
    em.map(lambda ext, *args, **kwargs: ext.plugin('Hello world!'))

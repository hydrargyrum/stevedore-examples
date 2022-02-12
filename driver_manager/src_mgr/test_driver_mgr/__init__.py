#!/usr/bin/env python3

import sys

import stevedore.driver


def format_and_print(extension, s):
    print(extension.plugin(s))


def main():
    try:
        driver_name = sys.argv[1]
    except IndexError:
        driver_name = 'plain'

    # `plugin_test_driver` is the name of the "rendez-vous" for all our drivers
    # each of our driver has a unique name, but all of them share the `plugin_test_driver` namespace
    # each of our driver should register itself to "plugin_test_driver"
    em = stevedore.driver.DriverManager('plugin_test_driver', driver_name)
    em.map(format_and_print, 'Hello world!')

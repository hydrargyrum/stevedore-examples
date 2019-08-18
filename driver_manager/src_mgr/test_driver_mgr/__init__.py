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

    em = stevedore.driver.DriverManager('plugin_test_driver', driver_name)
    em.map(format_and_print, 'Hello world!')

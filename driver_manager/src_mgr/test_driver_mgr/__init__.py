#!/usr/bin/env python3

import sys

import stevedore.driver


def main():
    try:
        driver_name = sys.argv[1]
    except IndexError:
        driver_name = 'plain'

    em = stevedore.driver.DriverManager('plugin_test_driver', driver_name)
    em(lambda ext: print(ext.plugin('Hello world!')))

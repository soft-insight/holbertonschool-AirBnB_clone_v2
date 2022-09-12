#!/usr/bin/python3
"""
Script that generates a clean function for out of date files
"""
from fabric.api import env, run, put, local

env.hosts = ['34.228.14.205', '34.226.205.34']
env.user = 'ubuntu'


def do_clean(number=0):
    '''delete function'''
    number = int(number)

    if number == 0 or number == 1:
        local('cd versions; ls | head -n -1 | xargs rm -rf')
        run('cd /data/web_static/releases ; ls | head -n -1 | xargs rm -rf')
    else:
        local('cd versions; ls | head -n -{} | xargs rm -rf'.format(number))
        run('cd /data/web_static/releases ; ls | head -n -2 | xargs rm -rf'.
            format(number))

# -*- coding:utf-8 -*-
"""
application bootstrap:
- read .env file to set system environment
- adapt settings values for Django app from heroku addons
- ...
"""
import sys
import os

import dotenv

import heroku_env


def bootstrap():
    """application bootstrap"""

    project_dir = os.path.dirname(__file__)
    # insert apps and libs into the system path
    sys.path.insert(0, os.path.join(project_dir, 'apps'))
    sys.path.insert(0, os.path.join(project_dir, 'libs'))

    dotenv.read_dotenv()

    # from envparse import Env
    # this converts (('Hoat Le', 'hoatle@teracy.com'),) to u'((Hoat Le, hoatle@teracy.com),))'
    # which is not expected
    # Env.read_envfile()

    heroku_env.set_env()

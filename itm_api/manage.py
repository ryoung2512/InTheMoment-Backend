#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from environs import Env
from django.core.management.commands.runserver import Command as runserver; 

env = Env()
env.read_env()

runserver.default_addr = env.str('LOCAL_IP', default='localhost')
runserver.default_port = env.str('PORT', default='8000')

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "itm_api.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

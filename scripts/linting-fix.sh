#!/bin/sh

# Attempt to fix the linting
black --target-version=py39 itm_api

# Run flake8 on directories
flake8 itm_api/

# Run black to see if all errors are gone
black --check --target-version=py39 itm_api
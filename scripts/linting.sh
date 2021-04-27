#!/bin/sh

# Run flake8 on directories
flake8 itm_api/
# Run black on directories
black --check --target-version=py39 itm_api/
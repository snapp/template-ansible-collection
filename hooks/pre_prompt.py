#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from datetime import datetime

config_path = 'cookiecutter.json'

try:
    with open(config_path, 'r') as file:
        data = json.load(file)

    # inject current year as a private variable
    data['_current_year'] = datetime.now().year

    with open(config_path, 'w') as file:
        json.dump(data, file, indent=4)
except FileNotFoundError:
    print(f"The file {config_path} was not found.")
except json.JSONDecodeError:
    print(f"Error decoding JSON from the file {config_path}.")
except Exception as e:
    print(f"An error occurred: {e}")

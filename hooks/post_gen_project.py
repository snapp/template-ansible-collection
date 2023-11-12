#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

REMOVE_PATHS = [
    {% if not cookiecutter.enable_antsibull_changelog %}
        '{{cookiecutter.collection_name}}/changelogs',
        '{{cookiecutter.collection_name}}/CHANGELOG.rst',
    {%- endif -%}
    {% if cookiecutter.license == 'none' %}
        '{{cookiecutter.collection_name}}/LICENSE',
    {% endif %}
]

for path in REMOVE_PATHS:
    path = path.strip()
    try:
        if path and os.path.exists(path):
            os.unlink(path) if os.path.isfile(path) else shutil.rmtree(path)
        else:
            print(f"Path not found: {path}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")

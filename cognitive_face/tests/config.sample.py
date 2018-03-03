#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: config.sample.py
Description: unittest configuration for Python SDK of the Cognitive Face API.

- Copy `config.sample.py` to `config.py`.
- Change the `BASE_URL` if necessary.
- Assign the `KEY` with a valid Subscription Key.
"""

# Subscription Key for calling the Cognitive Face API.
KEY = '9befd28a6c5842c49c5ec8d9b07474c5'

# Base URL for calling the Cognitive Face API.
# default is 'https://westus.api.cognitive.microsoft.com/face/v1.0/'
BASE_URL = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0'

# Time (in seconds) for sleep between each call to avoid exceeding quota.
# Default to 3 as free subscription have limit of 20 calls per minute.
TIME_SLEEP = 3

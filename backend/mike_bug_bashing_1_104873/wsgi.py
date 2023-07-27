"""
WSGI config for mike_bug_bashing_1_104873 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mike_bug_bashing_1_104873.settings')

application = get_wsgi_application()

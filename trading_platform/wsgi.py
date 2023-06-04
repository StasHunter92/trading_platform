"""
WSGI config for trading_platform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# ----------------------------------------------------------------------------------------------------------------------
# Set the DJANGO_SETTINGS_MODULE environment variable to the project's settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trading_platform.settings')

# ----------------------------------------------------------------------------------------------------------------------
# Create Django WSGI application
application = get_wsgi_application()

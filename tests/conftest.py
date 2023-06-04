import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trading_platform.settings")
django.setup()

# ----------------------------------------------------------------------------------------------------------------------
# Pytest settings
pytest_plugins = "tests.fixtures"

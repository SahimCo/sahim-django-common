"""Pytest configuration for sahim-django-common."""

import django
from django.conf import settings


def pytest_configure(config):
    """Configure Django settings for tests."""
    settings.configure(
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        INSTALLED_APPS=["sahim_django_common"],
        SECRET_KEY="test-secret-key-for-ci",
    )
    django.setup()

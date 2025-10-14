"""WSGI config for My Fairy Tale project."""
from __future__ import annotations

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_fairy_tale.settings")

application = get_wsgi_application()

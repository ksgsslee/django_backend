from .common import *

# debug toolbar
INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

INTERNAL_IPS = ["127.0.0.1"]

# cors
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000"
]

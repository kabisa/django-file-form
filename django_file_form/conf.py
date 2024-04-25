from django.conf import settings


# Cache timeout in seconds; default is 24 hours
CACHE_TIMEOUT = getattr(settings, "FILE_FORM_CACHE_TIMEOUT", 3600 * 24)

MAX_FILE_SIZE = getattr(settings, "FILE_FORM_MAX_FILE_SIZE", 3600 * 24)

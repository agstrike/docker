from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class AlwaysAuthenticatedMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            user, created = User.objects.get_or_create(username='demo')
            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, user)


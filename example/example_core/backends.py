from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class DemoBackend(ModelBackend):
    """Authenticate demo user with username and password 'demo'.
    """
    def authenticate(self, username=None, password=None):
        if username == 'demo' and password == 'demo':
            try:
                return User.objects.get(username='demo')
            except User.DoesNotExist:
                pass

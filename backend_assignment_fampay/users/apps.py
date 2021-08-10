from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UsersConfig(AppConfig):
    name = "backend_assignment_fampay.users"
    verbose_name = _("Users")
    def ready(self):
        try:
            import backend_assignment_fampay.users.signals  # noqa F401
        except ImportError:
            pass

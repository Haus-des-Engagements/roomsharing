from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "roomsharing.bookings"
    verbose_name = _("Bookings")

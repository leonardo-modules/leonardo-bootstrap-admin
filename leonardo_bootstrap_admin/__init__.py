
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


default_app_config = 'leonardo_bootstrap_admin.Config'

LEONARDO_ORDERING = 100

LEONARDO_APPS = [
    'leonardo_bootstrap_admin',
    'bootstrap_admin',
    'bootstrap_admin_feincms',
    'leonardo_admin',
]


class Config(AppConfig):
    name = 'leonardo_bootstrap_admin'
    verbose_name = _("Admin Bootstrap Theme")

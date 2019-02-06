from uuid import uuid4

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Application(models.Model):

    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE,
        related_name='apps', verbose_name=_("User")
    )
    name = models.CharField(_("Application name"), max_length=144)
    hook_url = models.URLField(_("Hook URL"))
    style_url = models.URLField(_("Style URL"))
    token = models.UUIDField(default=uuid4, editable=False)

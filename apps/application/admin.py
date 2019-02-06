from django.contrib import admin

from apps.application.models import Application


class ApplicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Application, ApplicationAdmin)

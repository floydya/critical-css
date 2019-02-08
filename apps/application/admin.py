from django.contrib import admin

from apps.application.models import Application


class ApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ('token',)
    list_display = ('id', 'name', 'user')
    list_filter = ('user',)


admin.site.register(Application, ApplicationAdmin)

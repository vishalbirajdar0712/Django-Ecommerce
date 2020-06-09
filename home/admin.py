from django.contrib import admin

# Register your models here.
from home.models import Setting ,Contact



class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','company','update_at','status']

admin.site.register(Setting,SettingAdmin)


admin.site.register(Contact)
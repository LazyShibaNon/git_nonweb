from django.contrib import admin

# Register your models here.

from .models import team_photo

class photoAdmin(admin.ModelAdmin):
    list_display = ('image','upload_date')
    
admin.site.register(team_photo,photoAdmin)
from django.contrib import admin
from .models import *
# Register your models here.

class userAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'middlename', 'lastname', 'email', 'public_key', )

admin.site.register(user, userAdmin)

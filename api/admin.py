from django.contrib import admin

# Register your models here.
from .models import Facebook
@admin.register(Facebook)
class FacebookAdmin(admin.ModelAdmin):
 list_display = ['id', 'user','followers','following','bio','likes']
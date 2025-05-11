from django.contrib import admin
from .models import Journal, DailyLog

# Register your models here.
admin.site.register(Journal)
admin.site.register(DailyLog)
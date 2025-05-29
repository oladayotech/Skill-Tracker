from django.contrib import admin
from .models import Journal, DailyLog, Profile

# Register your models here.
admin.site.register(Journal)
admin.site.register(DailyLog)
admin.site.register(Profile)
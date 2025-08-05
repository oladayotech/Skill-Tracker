from django.contrib import admin
from .models import Journal, Profile, Goal

# Register your models here.
admin.site.register(Journal)
admin.site.register(Goal)
# admin.site.register(DailyLog)
admin.site.register(Profile)
# admin.site.register(UserSelection)
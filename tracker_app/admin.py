from django.contrib import admin
from .models import Journal, DailyLog, Profile,UserSelection

# Register your models here.
admin.site.register(Journal)
admin.site.register(DailyLog)
admin.site.register(Profile)
admin.site.register(UserSelection)
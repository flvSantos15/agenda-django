from django.contrib import admin
from contact import models

@admin.register()
class ContactAdmin(admin.ModelAdmin):
  ...
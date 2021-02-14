from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from store.models.brands import Brand

class BrandAdmin(admin.ModelAdmin):
    model = Brand
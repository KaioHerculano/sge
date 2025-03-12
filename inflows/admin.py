from django.contrib import admin
from . import models


class InflowAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at', 'updated_at')
    search_fields = ('product__name', 'product__title',)


admin.site.register(models.Inflow, InflowAdmin)
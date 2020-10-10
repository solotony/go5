from django.contrib import admin
from ..models.customers import Customer


class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    fields = (
        ('first_name',  'patronymic_name', 'last_name', 'password'),
        ('email', 'phone', ),
        ('price_type', 'discount_policy', 'currency', ),
        ('discount_value', 'discount_valid_till', )
    )
    list_display = (
        '__str__', 'email', 'phone',
    )

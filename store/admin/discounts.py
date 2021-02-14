from django.contrib import admin
from ..models.discounts import DiscountPolicy, CumulativeStepping, PerOrderStepping

class CumulativeSteppingInline(admin.TabularInline):
    model = CumulativeStepping
    pass


class PerOrderSteppingInline(admin.TabularInline):
    model = PerOrderStepping
    pass


class DiscountPolicyAdmin(admin.ModelAdmin):
    inlines = (CumulativeSteppingInline, PerOrderSteppingInline, )
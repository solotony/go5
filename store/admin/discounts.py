from django.contrib import admin
from ..models.discounts import DiscountPolicy, DiscountPolicyStepping, PerOrderStepping

class DiscountPolicySteppingInline(admin.TabularInline):
    model = DiscountPolicyStepping
    pass


class PerOrderSteppingInline(admin.TabularInline):
    model = PerOrderStepping
    pass


class DiscountPolicyAdmin(admin.ModelAdmin):
    inlines = (DiscountPolicySteppingInline, PerOrderSteppingInline, )
from django.contrib import admin
from ..models.addresses import Address
from ..models.products import Product
from ..models.promos import Promo
from ..models.simple_entites import Stock, Supplier, Unit, Currency, PriceType, Country, Cluster
from django.utils.translation import gettext_lazy as _
from django.forms.models import BaseInlineFormSet
from django.urls import resolve
from functools import partial

admin.site.site_header = _('GO5 Administration')

from .characters import Character, CharacterAdmin
admin.site.register(Character, CharacterAdmin)

from .categories import Category, CategoryAdmin, MpttNode, MpttNodeAdmin
admin.site.register(MpttNode, MpttNodeAdmin)
admin.site.register(Category, CategoryAdmin)

from .customers import Customer, CustomerAdmin
admin.site.register(Customer, CustomerAdmin)

from .discounts import DiscountPolicy, DiscountPolicyAdmin
admin.site.register(DiscountPolicy, DiscountPolicyAdmin)

admin.site.register(Currency)
admin.site.register(Cluster)
admin.site.register(Country)
admin.site.register(PriceType)
admin.site.register(Stock)
admin.site.register(Unit)
admin.site.register(Supplier)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Promo)

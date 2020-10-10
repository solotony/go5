#    ____            _           _____
#   / ___|    ___   | |   ___   |_   _|   ___    _ __    _   _
#   \___ \   / _ \  | |  / _ \    | |    / _ \  | '_ \  | | | |
#    ___) | | (_) | | | | (_) |   | |   | (_) | | | | | | |_| |
#   |____/   \___/  |_|  \___/    |_|    \___/  |_| |_|  \__, |
#   1998-2020 (c) SoloTony.com                           |___/
#
#    ____           ____  _
#   |  _ \ _ __ ___/ ___|| |_ ___  _ __ ___
#   | |_) | '__/ _ \___ \| __/ _ \| '__/ _ \
#   |  __/| | | (_) |__) | || (_) | | |  __/
#   |_|   |_|  \___/____/ \__\___/|_|  \___|
#   v0.0  2020 (c) SoloTony.com/products/go5

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.db import models
from user.models import User
from .simple_entites import PriceType, Currency
from .discounts import DiscountPolicy
from ..exceptions import BadConfigirationError

class Customer(User):

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    price_type = models.ForeignKey(
        PriceType,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )

    discount_policy = models.ForeignKey(
        DiscountPolicy,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )

    currency = models.ForeignKey(
        Currency,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )

    discount_value = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        default=0
    )

    discount_valid_till = models.DateField(
        null=True,
        blank=True,
    )

    def is_registered_customer(self):
        return True

    customers_group = None

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not Customer.customers_group:
            Customer.customers_group = Group.objects.filter(name='customers').first()
        if not Customer.customers_group:
            raise BadConfigirationError(info=_('Group with name "customers" must exist'))
        self.groups.add(Customer.customers_group)


class AnonimousCustomer():

    def is_registered_customer(self):
        return True



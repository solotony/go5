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
from common.models.sluggable import SluggableMixin
from common.models.timestamps import TimestampsMixin
from common.models.seo import SeoMixin
from django.utils.translation import gettext_lazy as _
from .characters import Character, CharacterChoice
from .categories import Category
from .simple_entites import Stock, Supplier, PriceType, Currency, Unit
from .discounts import Cluster
from .taxes import TaxCluster
from user.models import User
from .customers import Customer

class Product(SeoMixin, TimestampsMixin, SluggableMixin):

    class Meta:
        app_label = 'store'
        verbose_name = _('Product')
        verbose_name_plural = _('Product')

    slug_base = 'name'
    seo_title_base = 'name'
    seo_description_base = 'name'
    route = 'catalog.product'

    articul = models.CharField(
        max_length=100,
        verbose_name=_('Аrticle'),
        unique=True
    )

    name = models.CharField(
        max_length=200,
        verbose_name=_('Product name'),
        null=False,
        blank=False,
    )

    cluster = models.ForeignKey(
        Cluster,
        verbose_name=_('Cluster'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    tax_cluster = models.ForeignKey(
        TaxCluster,
        verbose_name=_('Tax cluster'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    categories = models.ManyToManyField(
        Category,
        verbose_name=_('Categories'),
        related_name='product',
        related_query_name='products',
        blank=True,
    )

    master = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        verbose_name=_('Product'),
        related_name='skus',
        related_query_name='sku',
        null=True,
        blank=True,
    )

    components = models.ManyToManyField(
        'Product',
        verbose_name=_('Product'),
        related_name='complects',
        related_query_name='complect',
        blank=True,
    )

    digital = models.BooleanField(
        verbose_name=_('Digital'),
        default=False
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.DO_NOTHING,
        verbose_name=_('Unit'),
        related_name='products',
        related_query_name='product',
        null=False,
        blank=False,
    )

    package_volume = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        verbose_name=_('Package Volume'),
    )

    package_weight = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        verbose_name=_('Package Weight'),
    )

    package_count = models.PositiveIntegerField(
        verbose_name=_('Package Count'),
    )

    def __str__(self):
        return "{}: {}".format(self.articul, self.name)

    @classmethod
    def calculateComplects(cls):
        pass

    # # def actual_price(self, user:User):
    # #     if user.is_authenticated:
    # #         isinstance(user, Customer):
    # #
    # #         if
    #
    #
    #     pass


class Available:

    class Meta:
        app_label = 'store'
        verbose_name = _('Available')
        verbose_name_plural = _('Available')

    amount = models.PositiveIntegerField(
        verbose_name=_('Amount')
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Product'),
        related_name='availables',
        related_query_name='available',
        null=False,
        blank=False,
    )

    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        verbose_name=_('Stock'),
        related_name='availables',
        related_query_name='available',
        null=False,
        blank=False,
    )


class Booking:

    class Meta:
        app_label = 'store'
        verbose_name = _('Booking')
        verbose_name_plural = _('Bookings')

    amount = models.PositiveIntegerField(
        verbose_name=_('Amount')
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Product'),
        related_name='bookings',
        related_query_name='booking',
        null=False,
        blank=False,
    )

    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        verbose_name=_('Stock'),
        related_name='bookings',
        related_query_name='booking',
        null=False,
        blank=False,
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name=_('Supplier'),
        related_name='bookings',
        related_query_name='booking',
        null=False,
        blank=False,
    )


class Price(models.Model):

    class Meta:
        app_label = 'store'
        verbose_name = _('Price')
        verbose_name_plural = _('Prices')
        unique_together = ('type', 'product')

    # value in minimal currency unit (cent, kopeyka ...)
    value = models.BigIntegerField(
        verbose_name=_('Value'),
    )

    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        verbose_name=_('Currency'),
        related_name='prices',
        related_query_name='price',
    )

    type = models.ForeignKey(
        PriceType,
        on_delete=models.CASCADE,
        verbose_name=_('Price type'),
        related_name='prices',
        related_query_name='price',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Product'),
        related_name='prices',
        related_query_name='price',
    )

    computed = models.BooleanField(
        verbose_name=_('Complect computed price'),
    )



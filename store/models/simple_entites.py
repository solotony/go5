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
from django.conf import settings

class PreloadableModel(models.Model):

    class Meta:
        abstract=True

    by_id = dict()
    by_handle = dict()

    @classmethod
    def preload(cls):
        for obj in cls.objects.all():
            cls.by_id[obj.id] = obj
            cls.by_handle[obj.handle] = obj


class Stock(PreloadableModel):

    class Meta:
        app_label = 'store'
        verbose_name = _('Stock')
        verbose_name_plural = _('Stocks')

    name = models.CharField(
        max_length=200,
        verbose_name=_('Stock name')
    )

    handle = models.SlugField(
        max_length=32,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Handle'),
        help_text=_('case insensitive')
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.handle


class Supplier(PreloadableModel):

    class Meta:
        app_label = 'store'
        verbose_name = _('Supplier')
        verbose_name_plural = _('Suppliers')

    name = models.CharField(
        max_length=200,
        verbose_name=_('Supplier name')
    )

    handle = models.SlugField(
        max_length=32,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Handle'),
        help_text=_('case insensitive')
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.handle


class PriceType(PreloadableModel):
    """
Ценовая категория  предназначена для задания цен.  Например это могут быть розничные цены,
оптовые цены  нескольких видов цены. Каждому покупателю  должна быть назначена ценовая
категория по которой будут  продаваться товары этому покупателю. Если ценовая категория не
назначена на то будет действовать ценовая категория установленная по умолчанию для магазина.
    """

    class Meta:
        app_label = 'store'
        verbose_name = _('Price type') # Ценовая категория
        verbose_name_plural = _('Prices types')

    name = models.CharField(
        max_length=200,
        verbose_name=_('Price type title')
    )

    handle = models.SlugField(
        max_length=32,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Handle'),
        help_text=_('case insensitive')
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.handle


class Currency(PreloadableModel):

    class Meta:
        app_label = 'store'
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')

    name = models.CharField(
        max_length=200,
        verbose_name=_('Currency name')
    )

    symbol = models.CharField(
        max_length=10,
        verbose_name=_('Currency symbol')
    )

    symbol_before = models.BooleanField(
        default=False,
        verbose_name=_('Currency symbol before value')
    )

    handle = models.SlugField(
        max_length=32,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Handle'),
        help_text=_('case insensitive')
    )

    disabled = models.BooleanField(
        verbose_name=_('Disabled'),
        help_text=_('Currency is disabled for being used')
    )


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.handle


class Unit(PreloadableModel):
    """

    """
    class Meta:
        app_label = 'store'
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')

    name = models.CharField(
        max_length=200,
        verbose_name=_('Unit title')
    )

    symbol = models.CharField(
        max_length=200,
        verbose_name=_('Unit symbol')
    )

    handle = models.SlugField(
        max_length=32,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Handle'),
        help_text=_('case insensitive')
    )

    metric = models.BooleanField(
        verbose_name=_('Measurement system'),
        choices=((True,'Metric'),(False,'Us'))
    )

    type = models.CharField(
        verbose_name=_('Type'),
        max_length=20,
        choices=(('Item', 'Item'), ('Weight', 'Weight'), ('Length', 'Length'), ('Volume','Volume'), ('Voltage','Voltage'),
                 ('Power','Power'))
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.handle


class Cluster(PreloadableModel):
    """
Группа это альтернативная таксономия предназначенная для скидок и налогов.
Группы являются ортогональными то есть один товар не может входить более чем в одну группу.
Товары не входящие ни в одну из групп обрабатываются псевдогруппой "остальные товары".
Группы не являются заменой категориям или характеристикам.

Например для магазина на торгующего мебелью вы можете создать группы  "корпусная мебель"
и "кресла"  и каждый из них назначить свою скидочную политику.

Или для аптеки вы можете создать группу "Лекарственные средства"  и назначить для неё
отдельную налоговую схему.
    """
    class Meta:
        app_label = 'store'
        verbose_name = _('Cluster')
        verbose_name_plural = _('Clusters')

    name = models.CharField(
        max_length=200,
        verbose_name=_('Cluster title')
    )

    handle = models.SlugField(
        max_length=32,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Handle'),
        help_text=_('case insensitive')
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.handle


class Country(PreloadableModel):

    class Meta:
        app_label = 'store'
        verbose_name = _('Country')
        verbose_name_plural = _('Country')

    handle = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Country ISO Alpha-2 code')
    )

    name = models.CharField(
        max_length=200,
        verbose_name=_('Country name')
    )

    currency = models.ForeignKey(
        Currency,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        verbose_name = _('Currency')
    )

    language = models.CharField(
        max_length=2,
        choices=settings.LANGUAGES,
        verbose_name = _('Language'),
        null=True,
        blank=True,
        help_text = _('Only hardcoded languages available')
    )

    post_code_rule = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    disabled = models.BooleanField(
        verbose_name=_('Disabled'),
        default=False,
        help_text=_('Country is disabled for being used')
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.handle

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
from .simple_entites import PreloadableModel


class TaxPolicy(PreloadableModel):
    '''
Налоговая политика это принцип исчисления налога с товаров.
По умолчанию налог для товаров не указывается.
    '''

    class Meta:
        verbose_name = _('Tax policy')
        verbose_name_plural = _('Tax policies')

    vat = models.IntegerField(
        verbose_name=_('VAT'),
        help_text='VAT increase cost of product in pricelist. Prices are stored without VAT'
    )

    sales_tax = models.IntegerField(
        verbose_name='Salex TAX',
        help_text='Salex TAX increase cost of product in pricelist. Prices are stored without VAT'
    )

    smooth_cumulative = models.BooleanField(
        verbose_name='Smooth cumulative discount',
        default=True,
        help_text=''
    )

    smooth_per_order = models.BooleanField(
        verbose_name='Smooth per-order discount',
        default=True
    )


class TaxCluster(PreloadableModel):
    '''
Налоговый кластер это альтернативная таксономия предназначенная для налогов.
Налоговые кластеры являются ортогональными то есть один товар не может входить более чем в один налоговый кластер.
Товары не входящие ни в один из кластеров обрабатываются псевдо кластером 'остальные товары'.
Кластеры не являются заменой категориям или характеристикам.

Например для аптеки вы можете создать кластер 'Лекарственные средства'  и назначить для него
отдельную налоговую схему.
    '''

    class Meta:
        app_label = 'store'
        verbose_name = _('Тах cluster ')
        verbose_name_plural = _('Тах clusters')

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

    tax_policy = models.ForeignKey(
        to = TaxPolicy,
        on_delete=models.DO_NOTHING,
        verbose_name=_('Тах policy'),
        related_name='tax_cluster',
        related_query_name='tax_clusters'
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.handle

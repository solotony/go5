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

from django.utils.translation import gettext_lazy as _
from common.models.seo import SeoMixin
from common.models.sluggable import SluggableMixin
from common.models.timestamps import TimestampsMixin
from common.models.thumbnailed import ThumbnailedMixin
from store.models.simple_entites import PreloadableModelIcecat
from django.db import models
from django.shortcuts import reverse

class  Brand(SeoMixin, TimestampsMixin, ThumbnailedMixin, PreloadableModelIcecat):
    """
    Product brand
    """

    class Meta:
        app_label = 'store'
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    slug_base = 'name'
    seo_title_base = 'name'
    seo_description_base = 'name'
    route = 'catalog.brand'
    thumbnaled_image_folder = 'brands'
    thumbnaled_prefix = 'brand'

    name = models.CharField(
        null=False,
        blank=False,
        max_length=200,
        verbose_name=_('Brand name')
    )

    handle = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description')
    )

    icecat_id = models.BigIntegerField(
        verbose_name=_('IceCat ID'),
        db_index=True,
        null=True,
        blank=True,
        default=None
    )

    test = models.IntegerField(
        null=True,
    )

    def get_absolute_url(self):
        return reverse(self.route, self.slug)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.handle
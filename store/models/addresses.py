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
from .simple_entites import Country

class Address(models.Model):

    country = models.ForeignKey(
        Country,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        verbose_name=_('Country')
    )

    postcode = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name=_('Post code')
    )

    region = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_('Region')
    )

    city = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_('City')
    )

    address1 = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_('Street, Home')
    )

    address2 = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name=_('Office/Apartment/Room')
    )

    doorphone = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name=_('Doorphone')
    )

    comment = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name=_('Address comment')
    )

    latitude = models.DecimalField(
        max_digits=11,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name=_('Latitude')
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name=_('Longitude')
    )

    def __str__(self):
        s = str(self.country);
        if self.region:
            s += ', ' + self.region
        if self.postcode:
            s += ', ' + self.postcode
        if self.city:
            s += ', ' + self.city
        if self.address1:
            s += ', ' + self.address1
        if self.address2:
            s += ', ' + self.address2
        return s
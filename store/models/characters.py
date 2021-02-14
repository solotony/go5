#      ____            _           _____
#     / ___|    ___   | |   ___   |_   _|   ___    _ __    _   _
#     \___ \   / _ \  | |  / _ \    | |    / _ \  | '_ \  | | | |
#      ___) | | (_) | | | | (_) |   | |   | (_) | | | | | | |_| |
#     |____/   \___/  |_|  \___/    |_|    \___/  |_| |_|  \__, |
#     1998-2020 (c) SoloTony.com                           |___/
#
#    ____           ____  _
#   |  _ \ _ __ ___/ ___|| |_ ___  _ __ ___
#   | |_) | '__/ _ \___ \| __/ _ \| '__/ _ \
#   |  __/| | | (_) |__) | || (_) | | |  __/
#   |_|   |_|  \___/____/ \__\___/|_|  \___|
#   v0.0  2020 (c) SoloTony.com/products/go5


from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from .simple_entites import Unit

MAX_CHARACTERS = 63

class Character(models.Model):
    '''
    Класс реализует характеристики товара
    '''

    class Meta:
        verbose_name = _('Character')
        verbose_name_plural = _('Characters')
        app_label = 'store'
        unique_together=(('internal_name', 'unit'),)

    internal_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name=_('Internal character name'),
        help_text=_('used in admin panel')
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        verbose_name=_('Character\'s unit'),
    )

    handle = models.SlugField(
        max_length=32,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Hadle'),
        help_text=_('case insensitive')
    )

    public_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_('Public character name'),
        help_text=_('used in public interface')
    )

    help_text = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name=_('Help text'),
    )

    info = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Detailed description'),
    )

    filterable = models.BooleanField(
        default=True,
    )

    include_into_index_value = models.BooleanField(
        default=True,
    )

    include_into_index_name = models.BooleanField(
        default=True,
    )

    position = models.PositiveSmallIntegerField(
        editable=False,
        null=True,
        blank=True,
        verbose_name = _('Character position in search map'),
    )

    name = property(lambda self:self.public_name if self.public_name else self.internal_name)

    CHARACTER_TYPE_INHERITED = 0x1000
    CHARACTER_TYPE_INTEGER = 1
    CHARACTER_TYPE_FLOAT = 2
    CHARACTER_TYPE_DECIMAL1 = 3
    CHARACTER_TYPE_DECIMAL2 = 4
    CHARACTER_TYPE_DECIMAL3 = 5
    CHARACTER_TYPE_ENUM = 6
    CHARACTER_TYPE_STRING = 7
    CHARACTER_TYPE_SET = 8

    CHARACTER_TYPES = (
        (CHARACTER_TYPE_INTEGER, _('Integer value')),
        (CHARACTER_TYPE_FLOAT, _('Float value')),
        (CHARACTER_TYPE_DECIMAL1, _('Fixed decimal value, 1 digit after comma')),
        (CHARACTER_TYPE_DECIMAL2, _('Fixed decimal value, 2 digits after comma')),
        (CHARACTER_TYPE_DECIMAL3, _('Fixed decimal value, 3 digits after comma')),
        (CHARACTER_TYPE_ENUM, _('Enum')),
        (CHARACTER_TYPE_STRING, _('String value')),
        (CHARACTER_TYPE_SET, _('Set')),
    )

    _original_character_type = None

    character_type = models.IntegerField(
        null=False,
        blank=False,
        default=CHARACTER_TYPE_STRING,
        choices=CHARACTER_TYPES
    )

    icecat_id = models.BigIntegerField(
        verbose_name=_('IceCat ID'),
        db_index=True,
        null=True,
        blank=True,
        default=None
    )

    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)
        self._original_character_type = self.character_type

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.handle = self.handle.upper()  # Переводим значение в верхний регистр
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.internal_name

    def get_absolute_url(self):
        return reverse('catalog.character', args=[self.handle])



class CharacterChoice(models.Model):
    '''
    Класс реализует значения характеристик товара для
    типа CHARACTER_TYPE_ENUM и CHARACTER_TYPE_SET
    '''

    class Meta:
        verbose_name = _('Character choice')
        verbose_name_plural = _('Character choices')
        app_label = 'store'
        unique_together=['character', 'value']

    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        verbose_name=_('Character'),
        related_name='values'
    )

    value = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name=_('Character value')
    )

    def __str__(self):
        return self.value



#    ____            _           _____
#   / ___|    ___   | |   ___   |_   _|   ___    _ __    _   _
#   \___ \   / _ \  | |  / _ \    | |    / _ \  | '_ \  | | | |
#    ___) | | (_) | | | | (_) |   | |   | (_) | | | | | | |_| |
#   |____/   \___/  |_|  \___/    |_|    \___/  |_| |_|  \__, |
#   1998-2020 (c) SoloTony.com                           |___/
#   v 1.0.1
#   v 1.0.2


from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.fields import ThumbnailerImageField
from common.functions import get_upload_path
from easy_thumbnails.exceptions import InvalidImageFormatError, EasyThumbnailsError
import logging

logger = logging.getLogger()

class ThumbnailedMixin(models.Model):
    '''
Миксин добавляет поле image
необходимо задать:
thumbnaled_image_folder - для указания места хранения
thumbnaled_prefix - для указания префикса размера в настройках
    '''

    thumbnaled_image_folder = 'images'
    thumbnaled_prefix = None

    class Meta:
        abstract = True

    def _get_thumbnail_upload_path(self, filename):
        return get_upload_path(self.thumbnaled_image_folder, filename)

    image = ThumbnailerImageField(
        null=True,
        blank=True,
        verbose_name=_('Images'),
        upload_to=_get_thumbnail_upload_path,
    )

    def image_tag(self):
        if (self.image):
            try:
                thumb_url = get_thumbnailer(self.image.name)['admin'].url
                return  mark_safe('<img src="%s" />' % thumb_url)
            except InvalidImageFormatError as e:
                logger.error('image_tag({}) : {}'.format(self.image.name, str(e)))
                return None
            except EasyThumbnailsError as e:
                logger.error('image_tag({}) : {}'.format(self.image.name, str(e)))
                return None
        return None
    image_tag.short_description = 'Image preview'
    image_tag.allow_tags = True

    def image_big_url(self):
        if (self.image):
            try:
                return get_thumbnailer(self.image.name)[self.imaged_prefix+'.big'].url
            except InvalidImageFormatError as e:
                logger.error('image_big_url({}) : {}'.format(self.image.name, str(e)))
                return None
            except EasyThumbnailsError as e:
                logger.error('image_big_url({}) : {}'.format(self.image.name, str(e)))
                return None
        return None

    def image_small_url(self):
        if (self.image):
            try:
                return get_thumbnailer(self.image.name)[self.imaged_prefix+'.small'].url
            except InvalidImageFormatError as e:
                logger.error('image_small_url({}) : {}'.format(self.image.name, str(e)))
                return None
            except EasyThumbnailsError as e:
                logger.error('image_small_url({}) : {}'.format(self.image.name, str(e)))
                return None
        return None

    def image_tiny_url(self):
        if (self.image):
            try:
                return get_thumbnailer(self.image.name)[self.imaged_prefix+'.tiny'].url
            except InvalidImageFormatError as e:
                logger.error('image_tiny_url({}) : {}'.format(self.image.name, str(e)))
                return None
            except EasyThumbnailsError as e:
                logger.error('image_tiny_url({}) : {}'.format(self.image.name, str(e)))
                return None
        return None

    def image_thumb_url(self):
        if (self.image):
            try:
                return get_thumbnailer(self.image.name)[self.imaged_prefix+'.thumb'].url
            except InvalidImageFormatError as e:
                logger.error('image_thumb_url({}) : {}'.format(self.image.name, str(e)))
                return None
            except EasyThumbnailsError as e:
                logger.error('image_thumb_url({}) : {}'.format(self.image.name, str(e)))
                return None
        return None


#   v 1.0.1 - добавлены переводы
#   v 1.0.2 - добавлена обработка ошибок
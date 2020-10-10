#      ____            _           _____
#     / ___|    ___   | |   ___   |_   _|   ___    _ __    _   _
#     \___ \   / _ \  | |  / _ \    | |    / _ \  | '_ \  | | | |
#      ___) | | (_) | | | | (_) |   | |   | (_) | | | | | | |_| |
#     |____/   \___/  |_|  \___/    |_|    \___/  |_| |_|  \__, |
#     1998-2020 (c) SoloTony.com                           |___/

from django.db import models

# class UpperCharField(models.CharField):
#     '''
#     Custom uppercase CharField
#     '''
#
#     def get_prep_value(self, value):
#         value = super(UpperCharField, self).get_prep_value(value)
#         return value.upper()
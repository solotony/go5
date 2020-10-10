from django.db import models
from django.utils.translation import gettext_lazy as _
from store.models.module import *

class Message(models.Model):

    subject = models.CharField(
        max_length=200,
    )

    text = models.TextField(
        max_length=200,
    )




class Module:

    AUTHOR = 'Antonio Solo'
    VERSION = '0.1'


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Module, cls).__new__(cls)
        return cls.instance


    class INotify(AbstractINotify):

        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Module.INotify, cls).__new__(cls)
            return cls.instance

        def name(self):
            return _('Messanger module')

        def max_length(self) -> int:
            return 60000

        def accept_html(self) -> bool:
            return False

        def accept_images(self) -> bool:
            return True

        def accept_files(self) -> bool:
            return True

        def notify(self, user:AbstractIUser, message: str, files: list = None, images: list = None) -> str:
            pass

        def can_notify(self, user:AbstractIUser)->str:
            pass


    class IModule(AbstractIModule):

        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Module.IModule, cls).__new__(cls)
            return cls.instance

        def name(self):
            return _('Messanger module')

        def author(self):
            return Module.AUTHOR

        def version(self):
            return Module.VERSION

        def interfaces(self):
            return [Module.INotify]


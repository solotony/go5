#from django.db import models
from django.utils.translation import gettext_lazy as _
from store.models.module import *

class Module(AbstractIModule):

    AUTHOR = 'Antonio Solo'
    VERSION = '0.1'

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Module, cls).__new__(cls)
        return cls.instance


    class IEmailDelivery(AbstractIPay):

        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Module.IEmailDelivery, cls).__new__(cls)
            return cls.instance

        def name(self):
            return _('Email Delivery')


    class IHttpDelivery(AbstractIPay):

        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Module.IHttpDelivery, cls).__new__(cls)
            return cls.instance

        def name(self):
            return _('Http Delivery')


    class IModule(AbstractIModule):

        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Module.IModule, cls).__new__(cls)
            return cls.instance

        def name(self):
            return 'Virtual product module'

        def author(self):
            return Module.AUTHOR

        def version(self):
            return Module.VERSION

        def interfaces(self):
            return [Module.IEmailDelivery, Module.IHttpDelivery]


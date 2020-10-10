# from django.db import models
from django.utils.translation import gettext_lazy as _
from store.models.module import *


class Module:
    AUTHOR = 'Antonio Solo'
    VERSION = '0.1'

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Module, cls).__new__(cls)
        return cls.instance


    class ICourier(AbstractIDelivery):

        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Module.ICourier, cls).__new__(cls)
            return cls.instance

        def name(self):
            return _('Pickup')


    class IPayOnCourierDelivery(AbstractIPay):

        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Module.IPayOnCourierDelivery, cls).__new__(cls)
            return cls.instance

        def name(self):
            return _('Pay on pickup')

        def is_acceptable(self, delivery: AbstractIDelivery, order: AbstractIOrder):
            assert isinstance(order, AbstractIOrder)
            assert isinstance(delivery, AbstractIDelivery)
            return isinstance(delivery, Module.ICourier)


    class IModule(AbstractIModule):

        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Module.IModule, cls).__new__(cls)
            return cls.instance

        def name(self):
            return _('Courier delivery module')

        def author(self):
            return Module.AUTHOR

        def version(self):
            return Module.VERSION

        def interfaces(self):
            return [Module.ICourier, Module.IPayOnCourierDelivery]


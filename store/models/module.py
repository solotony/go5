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
from abc import ABC, ABCMeta, abstractmethod, abstractproperty

class Interface(ABC):
    """
    Базовый класс всех интерфейсов
    """
    pass


class AbstractIApplication(Interface):
    """
    Абстрактный базовый класс интерфейса приложения
    """
    @abstractmethod
    def version(self)->str:
        pass


class AbstractIProduct(Interface):
    """
    Абстрактный базовый класс интерфейса товара
    """
    @abstractmethod
    def name(self)->str:
        pass
    @abstractmethod
    def prices(self)->list:
        pass
    @abstractmethod
    def price(self, price_type)->int:
        pass


class AbstractIUser(Interface):
    """
    Абстрактный базовый класс интерфейса пользователя
    """
    @abstractmethod
    def name(self)->str:
        pass
    @abstractmethod
    def items(self)->list:
        pass


class AbstractIOrder(Interface):
    """
    Абстрактный базовый класс интерфейса заказа
    """
    @abstractmethod
    def name(self)->str:
        pass
    @abstractmethod
    def items(self)->list:
        pass


class AbstractIDelivery(Interface):
    """
    Абстрактный базовый класс интерфейса доставки
    """
    @abstractmethod
    def name(self)->str:
        pass


class AbstractIPay(Interface):
    """
    Абстрактный базовый класс интерфейса оплаты
    """
    @abstractmethod
    def name(self)->str:
        pass
    @abstractmethod
    def is_acceptable(self, delivery:AbstractIDelivery, order:AbstractIOrder)->bool:
        pass


class AbstractIDiscount(Interface):
    """
    Абстрактный базовый класс интерфейса скидки
    """
    @abstractmethod
    def name(self)->str:
        pass


class AbstractINotify(Interface):
    """
    Абстрактный базовый класс интерфейса уведомлений
    """
    @abstractmethod
    def name(self)->str:
        pass
    @abstractmethod
    def max_length(self) -> int:
        pass
    @abstractmethod
    def accept_html(self) -> bool:
        pass
    @abstractmethod
    def accept_images(self) -> bool:
        pass
    @abstractmethod
    def accept_files(self) -> bool:
        pass
    @abstractmethod
    def notify(self, user:AbstractIUser, message: str, files: list = None, images: list = None) -> str:
        pass
    @abstractmethod
    def can_notify(self, user:AbstractIUser)->str:
        pass


class AbstractIModule(ABC):
    """
    Абстрактный базовый класс интерфейса модуля
    """
    @abstractmethod
    def name(self)->str:
        pass
    @abstractmethod
    def author(self)->str:
        pass
    @abstractmethod
    def version(self)->str:
        pass
    @abstractmethod
    def interfaces(self)->list:
        pass

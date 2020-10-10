from django.core.management.base import BaseCommand
from store.models import Category, Character, CharacterValue, Stock, Supplier, Currency, PriceType, Unit, Cluster
from user.models import User
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


class Command(BaseCommand):
    help = "My shiny new management command."

    # def add_arguments(self, parser):
    #     parser.add_argument('seed', nargs='+')

    def create_demo(self):

        user = User.objects.create(first_name='Han', last_name='Solo', email='as@solotony.com',
                                   phone='+79119478909', is_active=True, is_superuser=True, is_staff=True)
        user.set_password('supaplex')
        user.save()

        clusters = {
            'food' :        Cluster(name=_('Food'), handle='FOOD'),
            'clothes':      Cluster(name=_('Сlothes'), handle='CLOTHES'),
            'medicines':    Cluster(name=_('Medicines'), handle='MEDICINES'),
            'equipment':    Cluster(name=_('Equipment'), handle='EQUIPMENT'),
        }

        stocks = [
            Stock(handle='LOCAL', name=_('Local Store')),
            Stock(handle='REMOTE', name=_('Remote Store'))
        ]

        for stock in stocks:
            stock.save()
        Stock.preload()

        suppliers = [
            Supplier(handle='ADIDAS', name=_('Adidas')),
            Supplier(handle='REEBOK', name=_('Reebok')),
            Supplier(handle='PNG', name=_('Proctor & Gamble')),
            Supplier(handle='PEPSI', name=_('Pepsi'))
        ]

        for supplier in suppliers:
            supplier.save()
        Supplier.preload()

        categories = [
            Category(name='ROOT'),  # 0
            Category(name='Спорттовары'),  # 1
            Category(name='Тренажеры'),  # 2
            Category(name='Механические'),  # 3
            Category(name='Электротренажеры'),  # 4
            Category(name='Спортинвентарь'),  # 5
            Category(name='Спортивное питание'),  # 6
            Category(name='Спортивная одежда'),  # 7
            Category(name='Спортивная обувь'),  # 8
            Category(name='Электротовары'),  # 9
            Category(name='Телевизоры'),  # 10
            Category(name='Пылесосы'),  # 11
            Category(name='Чайники'),  # 12
            Category(name='Продукты'),  # 13
            Category(name='Колбасы'),  # 14
            Category(name='Напитки'),  # 15
            Category(name='Пирожные'),  # 16
            Category(name='Одежда'),  # 17
            Category(name='Женская одежда'),  # 18
            Category(name='Мужская одежда'),  # 19
            Category(name='Детская одежда'),  # 20
            Category(name='Обувь'),  # 21
            Category(name='Женская обувь'),  # 22
            Category(name='Мужская обувь'),  # 23
            Category(name='Детская обувь'),  # 24
            Category(name='Кроссовки женские'),  # 25
            Category(name='Кроссовки мужские'),  # 26
        ]

        for category in categories:
            category.save()

        categories[1].parents.set([categories[0]])
        categories[2].parents.set([categories[1]])
        categories[3].parents.set([categories[2]])
        categories[4].parents.set([categories[2], categories[9]])
        categories[5].parents.set([categories[1]])
        categories[6].parents.set([categories[1], categories[13]])
        categories[7].parents.set([categories[1], categories[17]])
        categories[8].parents.set([categories[1], categories[21]])
        categories[9].parents.set([categories[0]])
        categories[10].parents.set([categories[9]])
        categories[11].parents.set([categories[9]])
        categories[12].parents.set([categories[9]])
        categories[13].parents.set([categories[0]])
        categories[14].parents.set([categories[13]])
        categories[15].parents.set([categories[13]])
        categories[16].parents.set([categories[13]])
        categories[17].parents.set([categories[0]])
        categories[18].parents.set([categories[17]])
        categories[19].parents.set([categories[17]])
        categories[20].parents.set([categories[17]])
        categories[21].parents.set([categories[0]])
        categories[22].parents.set([categories[21]])
        categories[23].parents.set([categories[21]])
        categories[24].parents.set([categories[21]])
        categories[25].parents.set([categories[8], categories[22]])
        categories[26].parents.set([categories[8], categories[23]])

        characters = [
            Character(internal_name='вес', handle='WEIGHT', filterable=True, position=1,  # 0
                      character_type=Character.CHARACTER_TYPE_DECIMAL3, unit=Unit.by_handle['KG']),
            Character(internal_name='марка', handle='BRAND', filterable=True, position=2,  # 1
                      character_type=Character.CHARACTER_TYPE_SET),
            Character(internal_name='цвет', handle='COLOR', filterable=True, position=3,  # 2
                      character_type=Character.CHARACTER_TYPE_SET),
            Character(internal_name='напряжение', handle='VOLTAGE', filterable=True, position=4,  # 3
                      character_type=Character.CHARACTER_TYPE_SET, unit=Unit.by_handle['V']),
            Character(internal_name='размер обуви', handle='SHOE_SIZE', filterable=True, position=5,  # 4
                      character_type=Character.CHARACTER_TYPE_INTEGER, public_name='размер'),
            Character(internal_name='размер одежды', handle='CLOSING_SIZE', filterable=True, position=6,  # 5
                      character_type=Character.CHARACTER_TYPE_SET, public_name='размер'),
            Character(internal_name='рост одежды', handle='CLOSING_GROWTH', filterable=True, position=7,  # 6
                      character_type=Character.CHARACTER_TYPE_INTEGER, unit=Unit.by_handle['CM'],
                      public_name='рост'),
            Character(internal_name='виды спорта', handle='SPORTS', filterable=True, position=8,  # 7
                      character_type=Character.CHARACTER_TYPE_SET),
            Character(internal_name='мощность', handle='POWER', filterable=True, position=9,  # 8
                      character_type=Character.CHARACTER_TYPE_INTEGER, unit=Unit.by_handle['W']),
            Character(internal_name='цвет одежды', handle='CLOSING_COLOR', filterable=True, position=10,  # 9
                      character_type=Character.CHARACTER_TYPE_SET, public_name='цвет'),
            Character(internal_name='материал подошвы', handle='SHOE_SOLE_MATERIAL', filterable=False, position=0,  # 10
                      character_type=Character.CHARACTER_TYPE_SET, public_name='подошва'),
            Character(internal_name='материал обуви', handle='SHOE_MATRIAL', filterable=False, position=0,  # 11
                      character_type=Character.CHARACTER_TYPE_SET, public_name='материал'),

        ]

        for character in characters:
            character.save()

        categories[0].characters.set([characters[1]])
        categories[1].characters.set([characters[7]])  # Спорттовары
        categories[9].characters.set([characters[3], characters[8]])  # Электротовары
        categories[13].characters.set([characters[0]])  # Продукты
        categories[17].characters.set([characters[5], characters[6], characters[9]])  # Одежда
        categories[21].characters.set([characters[4]])  # Обувь


    def create_generic(self):

        user = User.objects.create(first_name='Admin', last_name='Admin', email='demo@solotony.com',
                                   phone='+70000000000', is_active=True, is_superuser=True, is_staff=True)
        user.set_password('admin')
        user.save()

        customers = Group.objects.create(name='customers')
        partners = Group.objects.create(name='partners')

        # TODO all units
        units = [
            Unit(handle='ITEM', name=_('item'), symbol=_('it.'), metric=True, type='Item'),

            Unit(handle='KG', name=_('kilogram'), symbol=_('Kg'), metric=True, type='Weight'),
            Unit(handle='G', name=_('gram'), symbol=_('g'), metric=True, type='Weight'),
            Unit(handle='LBS', name=_('pound'), symbol=_('lbs'), metric=False, type='Weight'),

            Unit(handle='M', name=_('meter'), symbol=_('m'), metric=True, type='Length'),
            Unit(handle='CM', name=_('centimeter'), symbol=_('сm'), metric=True, type='Length'),
            Unit(handle='MM', name=_('millimeter'), symbol=_('сm'), metric=True, type='Length'),

            Unit(handle='L', name=_('liter'), symbol=_('l'), metric=True, type='Volume'),
            Unit(handle='ML', name=_('milliliter'), symbol=_('ml'), metric=True, type='Volume'),

            Unit(handle='V', name=_('volt'), symbol=_('v'), metric=True, type='Voltage'),

            Unit(handle='W', name=_('watt'), symbol=_('w'), metric=True, type='Power'),
        ]

        for unit in units:
            unit.save()
        Unit.preload()

        # TODO all currencies
        currencies = [
            Currency(handle='USD', name=_('US dollar'), symbol=_('$'), symbol_before=True),
            Currency(handle='EUR', name=_('Euro'), symbol=_('€'), symbol_before=False),
            Currency(handle='RUR', name=_('Russian ruble'), symbol=_('&#x20bd;'), symbol_before=False),
            Currency(handle='CNY', name=_('Renminbi'), symbol=_('&#xa5;'), symbol_before=False), #¥
            Currency(handle='JPY', name=_('Japanese yen'), symbol=_('&#xa5;'), symbol_before=False), #¥
            Currency(handle='GBP', name=_('Pound sterling'), symbol=_('&#xa3;'), symbol_before=False),  #£
        ]

        for currency in currencies:
            currency.save()
        Currency.preload()


        price_types = [
            PriceType(handle='RETAIL', name=_('Retail')),
            PriceType(handle='OLD', name=_('Retail old')),
            PriceType(handle='WHOLESALE', name=_('Wholesale')),
            PriceType(handle='PROMOTION', name=_('Promotion')),
        ]

        for price_type in price_types:
            price_type.save()
        PriceType.preload()



    def handle(self, *args, **options):
        self.create_generic()
        self.create_demo()



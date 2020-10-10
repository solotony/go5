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
from.simple_entites import Cluster
from django.utils.translation import gettext_lazy as _


class DiscountPolicy(models.Model):
    """
Скидочная политика это инструмент предоставления скидок на уровне пользователей.
Скидочная политика назначается  каждому пользователю  индивидуально и действует
на назначенную этому пользователю ценовую категорию.

Скидочная политика предусматривает два вида скидок: "постоянная скидка покупателям"
и "скидки на объем заказа".

Постоянная скидка покупателям может быть как плоской (значение скидки не зависит от объёма
продаж или контролируется вручную), так и накопительный, вычисляемой  в зависимости от
суммы заказов покупателя за определенный период. Скидки для для покупателей уменьшают
стоимость товара. При просмотре  каталога товаров, цены на товары отображаются уже с учетом
данной скидки.

Сглаживание кумулятивной скидки означает что при расчёте величина скидки на следующий
период скидка будет определяться линейный пропорцией между двумя шагами. До первого шага
скидка будет равной нулю, а после последнего значения последнего шага. Между шагами значение
скидки будет определяться по формуле

                       (discount2-discount1)*(sales-step1)
new_discount = step1 + -----------------------------------
                                 (step2-step1)

Скидка на объем заказа это альтернативный способ предоставления скидок. В отличие от скидок
предоставляемых покупателям  на постоянной основе,  скидки на на заказ предоставляются
в зависимости от от суммы сделанного заказа.
Как правило скидки на объем заказа предназначены для розничных покупателей.
Скидка на объем заказа выделяется в заказе отдельной строкой.

Если для скидки на объем заказа установлена  группа товаров то данная скидка будет
рассчитываться только на основании товаров включенных в данную группу


    """

    class Meta:
        verbose_name = 'Discount policy'
        verbose_name_plural = 'Discount policies'

    PREV_30_DAYS = 'PREV_30_DAYS'
    PREV_MONTH = 'PREV_MONTH'
    PREV_2_MONTHS = 'PREV_2_MONTHS'
    PREV_3_MONTHS = 'PREV_3_MONTHS'
    PREV_6_MONTHS = 'PREV_6_MONTHS'
    PREV_12_MONTHS = 'PREV_12_MONTHS'
    PREV_QUARTER = 'PREV_QUARTER'
    PREV_HALF = 'PREV_HALF'
    PREV_YEAR = 'PREV_YEAR'
    ALWAYS = 'ALWAYS'

    period_rule = models.CharField(
        max_length=20,
        null=False,
        choices=(
            (PREV_30_DAYS, 'PREV 30 DAYS'),
            (PREV_MONTH, 'PREV MONTH'),
            (PREV_2_MONTHS, 'PREV 2 MONTHS'),
            (PREV_3_MONTHS, 'PREV 3 MONTHS'),
            (PREV_6_MONTHS, 'PREV 6 MONTHS'),
            (PREV_12_MONTHS, 'PREV 12 MONTHS'),
            (PREV_QUARTER, 'PREV QUARTER'),
            (PREV_HALF, 'PREV HALF'),
            (PREV_YEAR, 'PREV YEAR'),
            (ALWAYS, 'ALWAYS'),
        ),
        verbose_name="Discount period basis"
    )

    cluster = models.ForeignKey(
        Cluster,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        verbose_name="Products cluster"
    )

    smooth_cumulative = models.BooleanField(
        verbose_name="Smooth cumulative discount",
        default=True,
        help_text=""
    )

    smooth_per_order = models.BooleanField(
        verbose_name="Smooth per-order discount",
        default=True
    )


class DiscountPolicyStepping(models.Model):

    class Meta:
        verbose_name = 'Cumulative orders summ step'
        verbose_name_plural = 'Cumulative orders summ steps'

    discount_policy = models.ForeignKey(
        DiscountPolicy,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Discount policy"
    )

    step = models.BigIntegerField(
        null=False,
        blank=False,
        verbose_name="Cumulative orders summ"
    )

    percentage = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        null=False,
        blank=False,
        verbose_name="Discount value"
    )


class PerOrderStepping(models.Model):

    class Meta:
        verbose_name = 'Order summ step'
        verbose_name_plural = 'Order summ steps'

    discount_policy = models.ForeignKey(
        DiscountPolicy,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Discount policy"
    )

    step = models.BigIntegerField(
        null=False,
        blank=False,
        verbose_name="Order summ"
    )

    percentage = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        null=False,
        blank=False,
        verbose_name="Discount value"
    )
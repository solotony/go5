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


from typing import List, Union
from django.db import models
from django.db.models.query import Q
from django.shortcuts import reverse
import logging
from django.utils.translation import gettext_lazy as _
from common.models.seo import SeoMixin
from common.models.sluggable import SluggableMixin
from common.models.timestamps import TimestampsMixin
from cached_property import cached_property
from .characters import Character
from .simple_entites import Supplier, Stock


WEBSITE_ROOT_CATEGORY_ID = 1
WEBSITE_TREE_ID = 0
WEBSITE_INHERITERS_TREE_ID = 1

EMPTY_QUERY = """
    DELETE
    FROM %(rel_table)s
    WHERE 1
"""

logger = logging.getLogger()


class MpttNodeManager(models.Manager):

    class Meta:
        app_label = 'store'

    def empty(self):
        """
        Полная очистка MPTT дерева
        """
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(EMPTY_QUERY % {'rel_table':self.model._meta.db_table})


class MpttNode(models.Model):
    """
    Класс для работы с деревом категорий
    """
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        editable=True,
        db_index=True
    )

    tree_id = models.IntegerField(
        db_index=True
    )

    inheriters_tree = models.BooleanField(
        db_index=True
    )

    mptt_left = models.IntegerField(
        db_index=True
    )

    mptt_right = models.IntegerField(
        db_index=True
    )

    mptt_level = models.IntegerField(
        db_index=True
    )

    objects = MpttNodeManager()

    def __str__(self):
        return "category_id={}, tree_id={}, inheriters_tree={}, mptt_left={}, mptt_right={}, mptt_level={}".format(
            self.category_id, self.tree_id, self.inheriters_tree, self.mptt_left,self.mptt_right, self.mptt_level)


class CategoryCharacterPivot(models.Model):
    """
    Связь категорий с характеристиками
    """
    class Meta:
        app_label = 'store'
        verbose_name = _('Category character')
        verbose_name_plural = _('Category characters')

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE
    )

    character = models.ForeignKey(
        'Character',
        on_delete=models.CASCADE
    )

    deleted = models.BooleanField(
        default=False
    )


class ParentPivot(models.Model):
    """
    Связь дочерних и родительских категорий
    """
    class Meta:
        app_label = 'store'
        verbose_name = _('Parent category')
        verbose_name_plural = _('Parent categories')
        pass

    child = models.ForeignKey(
        'Category',
        related_name='parent_refs',
        on_delete=models.CASCADE,
        verbose_name=_('Child category'),
    )

    parent = models.ForeignKey(
        'Category',
        related_name='child_refs',
        on_delete=models.CASCADE,
        verbose_name=_('Parent category'),
    )

    inheritance = models.BooleanField(
        default = True,
        verbose_name=_('Character inheritance'),
        help_text = _('***help_text*** Character inheritance')
    )

    @classmethod
    def all_as_dict(cls):
        parents_dict = dict()
        for node in cls.objects.all():
            childs = parents_dict.get(node.parent_id)
            if not childs:
                parents_dict[node.parent_id] = childs = set()
            childs.add((node.child_id, node.inheritance))
        return parents_dict


class CategoryManger(models.Manager):

    def descendant_ids(self, category_id:int)->List[int]:
        pass


class Category(SeoMixin, SluggableMixin, TimestampsMixin):
    class Meta:
        app_label = 'store'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    slug_base = 'name'
    seo_title_base = 'name'
    seo_description_base = 'name'
    route = 'catalog.category'

    objects = CategoryManger()

    name = models.CharField(
        null=False,
        blank=False,
        max_length=200,
        verbose_name=_('Category title')
    )

    has_products = models.BooleanField(
        default=True,
        verbose_name=_('Has products'),
        help_text=_('***help_text*** Has products')
    )

    show_products = models.BooleanField(
        default=True,
        verbose_name=_('Show products'),
        help_text=_('***help_text*** Show products')
    )

    show_subcategory_products = models.BooleanField(
        default=True,
        verbose_name=_('Show subcategories products'),
        help_text=_('***help_text*** Show subcategories products')
    )

    custom_characters = models.BooleanField(
        default=False,
        verbose_name=_('Custom characters'),
        help_text=_('***help_text*** Custom characters')
    )

    parents = models.ManyToManyField(
        'Category',
        verbose_name=_('Parent categories'),
        related_name='childs',
        related_query_name='child',
        through='ParentPivot',
        through_fields=('child', 'parent'),
    )

    characters = models.ManyToManyField(
        'Character',
        through='CategoryCharacterPivot',
        through_fields=('category', 'character'),
        verbose_name=_('Custom category characters')
    )

    default_supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        related_name='categories',
        related_query_name='category',
        null=True,
        blank=True,
        default=None,
        verbose_name=_('Default Supplier')
    )

    default_stock = models.ForeignKey(
        Stock,
        on_delete=models.SET_NULL,
        related_name='categories',
        related_query_name='category',
        null=True,
        blank=True,
        default=None,
        verbose_name=_('Default Supplier')
    )

    default_digital = models.NullBooleanField(
        null=True,
        blank=True,
        default=None,
        verbose_name=_('Default digital')
    )

    def __str__(self):
        if self.name:
            return str(self.name)
        else:
            if self.id:
                return _('Unnamed category #' + str(self.id))
            else:
                return _('New category')

    @classmethod
    def possible_parents_qs(cls, instance):
        if (instance):
            return cls.objects.exclude(id=instance.id)
        else:
            return cls.objects

    @classmethod
    def possible_childs_qs(cls, instance):
        if (instance):
            return cls.objects.exclude(id=instance.id).exclude(id=1)
        else:
            return cls.objects.exclude(id=1)

    @classmethod
    def all_as_dict(cls):
        _dict = dict()
        for category in cls.objects.all():
            _dict[category.id] = category
        return _dict

    _categories_dict = None
    _relations = None

    @classmethod
    def _build_tree(cls, tree_id:int, category_id:int, left:int, parent_level:int, inheriters_tree:bool=False)->int:
        logger.debug('_build_tree [tree_id={}, category_id={}, left={}, parent_level={}, inheriters_tree={}'.format(
            tree_id, category_id, left, parent_level, inheriters_tree))
        tree_node = MpttNode(tree_id=tree_id, inheriters_tree=inheriters_tree, category_id=category_id,
                             mptt_level=parent_level+1, mptt_left=left, mptt_right=left+1)
        category = cls._categories_dict[category_id]
        assert(category)
        childs = cls._relations.get(category_id)
        if childs:
            for child in childs:
                if not inheriters_tree or child[1]:
                    tree_node.mptt_right = \
                        cls._build_tree(tree_id, child[0], tree_node.mptt_right, tree_node.mptt_level, inheriters_tree)
        cls.node_list.append(tree_node)
        return tree_node.mptt_right + 1

    @classmethod
    def build_tree(cls):
        logger.debug('build_tree')
        cls._categories_dict = cls.all_as_dict()
        cls._relations = ParentPivot.all_as_dict()
        cls.node_list = list()
        MpttNode.objects.empty()
        cls._build_tree(WEBSITE_TREE_ID, WEBSITE_ROOT_CATEGORY_ID, 1, 0, False)
        cls._build_tree(WEBSITE_TREE_ID, WEBSITE_ROOT_CATEGORY_ID, 1, 0, True)
        MpttNode.objects.bulk_create(cls.node_list)
        pass

    def get_absolute_url(self):
        if self.id == self.get_root_category_id():
            return reverse('catalog.root')
        else:
            return reverse('catalog.category', args=[self.slug])


    @cached_property
    def descendants_tree_node(self):
        """элемент в дереве потомков"""
        logger.debug('descendants_tree_node id=[{}] self=[{}]'.format(str(self.id), self))
        res = MpttNode.objects.filter(category_id=self.id).\
            filter(tree_id=WEBSITE_TREE_ID). \
            filter(inheriters_tree=False). \
            first()
        assert(res)
        logger.debug('descendants_tree_node res=' + str(res))
        return res

    is_descendants = property(
        lambda self : self.descendants_tree_node.mptt_right > self.descendants_tree_node.mptt_left + 1
    )

    @cached_property
    def inheriters_tree_node(self):
        """элемент в дереве наследников"""
        logger.debug('inheriters_tree_node id={} self={}'.format(str(self.id), self))
        res = MpttNode.objects.filter(category_id=self.id).\
            filter(tree_id=WEBSITE_TREE_ID). \
            filter(inheriters_tree=True). \
            first()
        assert (res)
        logger.debug('inheriters_tree_node res=' + str(res))
        return res

    is_inheriters = property(
        lambda self : self.inheriters_tree_node.mptt_right > self.inheriters_tree_node.mptt_left + 1
    )

    @cached_property
    def all_descendants_tree_nodes_qs(self):
        """все элементы в дереве потомков"""
        logger.debug('all_descendants_tree_nodes_qs id={} self={}'.format(str(self.id), self))
        res = MpttNode.objects.filter(category_id=self.id). \
            filter(tree_id=WEBSITE_TREE_ID). \
            filter(inheriters_tree=False)
        return res

    @cached_property
    def all_inheriters_tree_node_qs(self):
        """элемент в дереве наследников"""
        logger.debug('all_inheriters_tree_node_qs id={} self={}'.format(str(self.id), self))
        res = MpttNode.objects.filter(category_id=self.id).\
            filter(tree_id=WEBSITE_TREE_ID). \
            filter(inheriters_tree=True)
        return res

    @cached_property
    def descendants_ids_qs(self)->Union[None, models.QuerySet]:
        """Список уникальных идентификаторов потомков"""
        logger.debug('descendants_ids_qs self={}'.format(str(self)))
        if not self.is_descendants:
            return None
        return MpttNode.objects.filter(mptt_left__gt=self.descendants_tree_node.mptt_left).\
            filter(mptt_right__lt=self.descendants_tree_node.mptt_right). \
            filter(tree_id=WEBSITE_TREE_ID). \
            filter(inheriters_tree=False). \
            values('category_id').distinct()

    @cached_property
    def descendants_qs(self)->Union[None, models.QuerySet]:
        """Список потомков. Возвращаемые объекты - категории."""
        if not self.is_descendants:
            return None
        logger.debug('descendants_qs self={}'.format(str(self)))
        return Category.objects.filter(id__in=self.descendants_ids_qs)

    @cached_property
    def descendants_tree_qs(self)->Union[None, models.QuerySet]:
        """Полное дерево потомков. Возвращаемые объекты - элементы дерева."""
        if not self.is_descendants:
            return None
        logger.debug('descendants_tree_qs self={}'.format(str(self)))
        return MpttNode.objects.filter(mptt_left__gt=self.descendants_tree_node.mptt_left).\
            filter(mptt_right__lt=self.descendants_tree_node.mptt_right).prefetch_related('category').\
            filter(tree_id=WEBSITE_TREE_ID). \
            filter(inheriters_tree=False). \
            order_by('mptt_left')

    @cached_property
    def inheriters_ids_qs(self)->Union[None, models.QuerySet]:
        """Список уникальных идентификаторов наследников"""
        logger.debug('inheriters_ids_qs self={}'.format(str(self)))
        if not self.is_inheriters:
            return None
        return MpttNode.objects.filter(mptt_left__gt=self.inheriters_tree_node.mptt_left).\
            filter(mptt_right__lt=self.inheriters_tree_node.mptt_right). \
            filter(tree_id=WEBSITE_TREE_ID). \
            filter(inheriters_tree=True). \
            values('category_id').distinct()

    @cached_property
    def inheriters_tree_qs(self)->Union[None, models.QuerySet]:
        """Полное дерево наследников. Возвращаемые объекты - элементы дерева."""
        if not self.is_descendants:
            return None
        logger.debug('inheriters_tree_qs self={}'.format(str(self)))
        return MpttNode.objects.filter(mptt_left__gt=self.inheriters_tree_node.mptt_left).\
            filter(mptt_right__lt=self.inheriters_tree_node.mptt_right).prefetch_related('category').\
            filter(tree_id=WEBSITE_TREE_ID). \
            filter(inheriters_tree=True). \
            order_by('mptt_left')

    @cached_property
    def is_predecessors(self):
        return self.parents.exists

    @cached_property
    def is_ancestors(self):
        return self.parents.exists

    @cached_property
    def predecessors_ids_qs(self)->Union[None, models.QuerySet]:
        """Список уникальных идентификаторов предшественников"""
        logger.debug('predecessors_ids_qs self={}'.format(str(self)))
        if not self.is_predecessors:
            return None
        result_qs = None
        for tree_node in self.all_descendants_tree_nodes_qs.all():
            qs = MpttNode.objects.\
            filter(mptt_left__lt=tree_node.mptt_left).\
            filter(mptt_right__gt=tree_node.mptt_right). \
            filter(tree_id=WEBSITE_TREE_ID). \
            filter(inheriters_tree=False). \
            values('category_id').distinct()
            logger.debug('predecessors_ids_qs qs={}'.format(str(qs.query)))
            if not result_qs:
                result_qs = qs
            else:
                result_qs = result_qs.union(qs).distinct()
        logger.debug('predecessors_ids_qs res={}'.format(str(result_qs.query)))
        return result_qs

    @cached_property
    def predecessors_qs(self)->Union[None, models.QuerySet]:
        """Список предшественников. Возвращаемые объекты - категории."""
        logger.debug('predecessors_qs self={}'.format(str(self)))
        return Category.objects.filter(id__in=self.predecessors_ids_qs)

    @cached_property
    def ancestors_ids_qs(self)->Union[None, models.QuerySet]:
        """Список уникальных идентификаторов предков"""
        logger.debug('ancestors_ids_qs self={}'.format(str(self)))
        if not self.is_ancestors:
            return None
        result_qs = None
        for tree_node in self.all_inheriters_tree_node_qs.all():
            qs = MpttNode.objects.\
            filter(mptt_left__lt=tree_node.mptt_left).\
            filter(mptt_right__gt=tree_node.mptt_right). \
            filter(tree_id=WEBSITE_TREE_ID). \
            filter(inheriters_tree=True). \
            values('category_id').distinct()
            if not result_qs:
                result_qs = qs
            else:
                result_qs = result_qs.union(qs).distinct()
        return result_qs

    @cached_property
    def ancestors_qs(self)->Union[None, models.QuerySet]:
        """Список предков. Возвращаемые объекты - категории."""
        logger.debug('ancestors_qs self={}'.format(str(self)))
        if not self.ancestors_ids_qs:
            return None
        return Category.objects.filter(id__in=self.ancestors_ids_qs)

    @cached_property
    def ancestors_characters_qs(self):
        logger.debug('ancestors_characters_qs self={}'.format(str(self)))
        if not self.ancestors_ids_qs:
            return None
        return Character.objects.filter(categorycharacterpivot__category_id__in=self.ancestors_ids_qs).distinct()

    @cached_property
    def all_characters_qs(self):
        logger.debug('all_characters_qs self={}'.format(str(self)))
        return Character.objects.filter(Q(categorycharacterpivot__category_id__in=self.ancestors_ids_qs)|Q(categorycharacterpivot__category_id=self.id) ).distinct()


    @classmethod
    def get_root_category_id(cls):
        return WEBSITE_ROOT_CATEGORY_ID

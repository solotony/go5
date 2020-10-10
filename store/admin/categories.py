from django.contrib import admin
from ..models.categories import Category, MpttNode
from django.utils.translation import gettext_lazy as _

class ParentsInlineAdmin(admin.TabularInline):
    model = Category.parents.through
    fk_name = "child"
    can_delete = True
    extra = 1
    classes = ['collapse']

    def __init__(self, *args, **kwargs):
        super(ParentsInlineAdmin, self).__init__(*args, **kwargs)
        self.instance = None

    def get_formset(self, request, obj=None, **kwargs):
        self.instance = obj
        return super(ParentsInlineAdmin, self).get_formset(request, obj, **kwargs)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ParentsInlineAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == "parent":
            formfield.queryset = Category.possible_parents_qs(self.instance)
        return formfield


#TODO убрать кнопки "
class ChildsInlineAdmin(admin.TabularInline):
    model = Category.childs.through
    fk_name = "parent"
    can_delete = True
    extra = 1
    classes = ['collapse']
    verbose_name = _('Child category')
    verbose_name_plural = _('Child categories')

    def __init__(self, *args, **kwargs):
        super(ChildsInlineAdmin, self).__init__(*args, **kwargs)
        self.instance = None

    def get_formset(self, request, obj=None, **kwargs):
        self.instance = obj
        return super(ChildsInlineAdmin, self).get_formset(request, obj, **kwargs)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ChildsInlineAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == "child":
            formfield.queryset = Category.possible_childs_qs(self.instance)
        return formfield


class CharacterInlineAdmin(admin.TabularInline):
    model = Category.characters.through
    fk_name = "category"
    can_delete = True
    extra = 1
    classes = ['collapse']
    # verbose_name = _('Child category')
    # verbose_name_plural = _('Child categories')

    def __init__(self, *args, **kwargs):
        super(CharacterInlineAdmin, self).__init__(*args, **kwargs)
        self.instance = None

    def get_formset(self, request, obj=None, **kwargs):
        self.instance = obj
        return super(CharacterInlineAdmin, self).get_formset(request, obj, **kwargs)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(CharacterInlineAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        # if db_field.name == "child":
        #     formfield.queryset = Category.possible_childs_qs(self.instance)
        return formfield


#TODO убрать кнопки "
class CategoryAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('name', 'slug')
        }),
        (_('Options'), {
            'classes': ('collapse',),
            'fields':('has_products', 'show_products', 'show_subcategory_products', 'custom_characters')
        }),
        (_('SEO'), {
            'classes': ('collapse',),
            'fields': ('_seo_title', '_seo_description')
        }),
    )

    prepopulated_fields = {'slug':('name',)}

    inlines = [ParentsInlineAdmin, ChildsInlineAdmin, CharacterInlineAdmin]

    view_on_site = True

    def __init__(self, *args, **kwargs):
        super(CategoryAdmin, self).__init__(*args, **kwargs)
        self.instance = None

    # def get_fieldsets(self, request, obj=None):
    #     self.instance = obj
    #     return super(CategoryAdmin, self).get_fieldsets(request, obj)
    #
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "parent":
    #         kwargs["queryset"] = Category.possible_parents_qs(self.instance)
    #     return super(CategoryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    change_form_template = 'store/admin/change_form.html'


class MpttNodeAdmin(admin.ModelAdmin):
    model = MpttNode
    list_display = ['category', 'tree_id', 'inheriters_tree', 'mptt_left', 'mptt_right', 'mptt_level']
    readonly_fields = ['category', 'tree_id', 'inheriters_tree', 'mptt_left', 'mptt_right', 'mptt_level']

    def get_queryset(self, request):
        qs = super(MpttNodeAdmin, self).get_queryset(request)
        return qs.prefetch_related('category')
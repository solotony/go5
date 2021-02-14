from django.contrib import admin
from ..models.characters import Character, CharacterChoice

class CharacterChoiceInline(admin.TabularInline):
    model = CharacterChoice


class CharacterAdmin(admin.ModelAdmin):
    model = Character
    inlines = [CharacterChoiceInline]
    prepopulated_fields = {"handle": ("internal_name",)}

    def get_inline_instances(self, request, obj:Character=None):
        inline_instances = []
        for inline_class in self.get_inlines(request, obj):
            inline = inline_class(self.model, self.admin_site)
            if request:
                if not obj or obj._original_character_type != obj.CHARACTER_TYPE_SET:
                    continue
                if not (inline.has_view_or_change_permission(request, obj) or
                        inline.has_add_permission(request, obj) or
                        inline.has_delete_permission(request, obj)):
                    continue
                if not inline.has_add_permission(request, obj):
                    inline.max_num = 0
            inline_instances.append(inline)

        return inline_instances

    def get_formsets_with_inlines(self, request, obj:Character=None):
        for inline in self.get_inline_instances(request, obj):
            # hide/show market-specific inlines based on market name
            if obj and obj._original_character_type == obj.CHARACTER_TYPE_SET:
                yield inline.get_formset(request, obj), inline
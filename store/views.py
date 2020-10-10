from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, TemplateView
from store.models import Category


class CategoryView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'default/pages/category.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('parents').prefetch_related('childs')


class CategoryRootView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'default/pages/category.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('parents').prefetch_related('childs')

    def get_object(self, queryset=None):
        self.kwargs[self.pk_url_kwarg] = Category.get_root_category_id()
        return super().get_object(queryset)


class ProductView(DetailView):
    pass


class FrontView(TemplateView):
    template_name = 'default/pages/front.html'



def buildtree(request):
    Category.build_tree()
    return render(request, 'default/x_buildtree.html', {
    })

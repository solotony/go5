from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('category/', views.CategoryRootView.as_view(), name='catalog.root'),
    path('category/<slug>', views.CategoryView.as_view(), name='catalog.category'),
    path('product/<slug>', views.ProductView.as_view(), name='catalog.product'),
    re_path('^$', views.FrontView.as_view(), name='catalog.front'),

    path('buildtree', views.buildtree, name='buildtree'),
]

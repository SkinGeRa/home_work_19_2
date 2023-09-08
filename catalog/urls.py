from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, index, product

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product')
]

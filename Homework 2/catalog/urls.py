from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail')
]

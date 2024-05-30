from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView, PostCreateView, PostListView, \
    PostDetailView, PostUpdateView, PostDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('blog/create', PostCreateView.as_view(), name='post_create'),
    path('blog/', PostListView.as_view(), name='posts_list'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('blog/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('blog/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]

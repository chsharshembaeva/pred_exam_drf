from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register('category', views.CategoryViewSet, basename='category')

urlpatterns = [
    # path('', include(router.urls)),
    path('category/', views.CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('category/<int:category_id>/item/', views.ItemListCreateAPIView.as_view()),
    path('category/<int:category_id>/item/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view()),
    path('category/<int:category_id>/item/<int:item_id>/order/', views.ItemOrder.as_view()),
]


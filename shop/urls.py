from django.urls import path, include


from . import views


urlpatterns = [
    path('category/', views.CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('category/<int:category_id>/item/', views.ItemListCreateAPIView.as_view()),
    path('category/<int:category_id>/item/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view()),
    path('category/<int:category_id>/item/<int:item_id>/order/', views.OrderListCreateAPIView.as_view()),
    path('category/<int:category_id>/item/<int:item_id>/order/<int:pk>/', views.OrderRetrieveUpdateDestroyAPIView.as_view()),
]

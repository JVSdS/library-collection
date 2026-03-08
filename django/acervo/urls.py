from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('itens/', views.item_list, name='item_list'),
    path('item/novo/', views.item_create, name='item_create'),
    path('item/<int:pk>/editar/', views.item_update, name='item_update'),
    path('item/<int:pk>/deletar/', views.item_delete, name='item_delete'),
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('registro/', views.registrar, name='registro'),
]
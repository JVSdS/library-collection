from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('itens/', views.item_list, name='item_list'),
    path('item/novo/', views.item_create, name='item_create'),
    path('item/<int:pk>/editar/', views.item_update, name='item_update'),
    path('item/<int:pk>/deletar/', views.item_delete, name='item_delete'),
    path('registro/', views.registrar, name='registro'),
    path('meus-favoritos/', views.meus_favoritos, name='meus_favoritos'),
    path('favoritar/<int:item_id>/', views.adicionar_favorito, name='adicionar_favorito'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('perfil/nota/<int:favorito_id>/', views.atualizar_nota, name='atualizar_nota'),
    path('remover-favorito/<int:favorito_id>/', views.remover_favorito, name='remover_favorito'),
    path('atualizar-nota/<int:favorito_id>/', views.atualizar_nota, name='atualizar_nota'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Perfil, Item

@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def salvar_perfil(sender, instance, **kwargs):
    instance.perfil.save()

@receiver(post_save, sender=Item)
def item_post_save(sender, instance, created, **kwargs):
    if created:
        tipo_nome = instance.tipo.nome if instance.tipo else "Sem Tipo"
        print(f"Novo item registrado: {instance.titulo} ({tipo_nome})")
    else:
        print(f"Registro de {instance.titulo} foi atualizado no acervo.")
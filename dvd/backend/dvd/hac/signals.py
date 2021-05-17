from django.db.models.signals import post_save
from graphene_subscriptions.signals import post_save_subscription

from .models import HiveCatalogue

post_save.connect(post_save_subscription, sender=HiveCatalogue, dispatch_uid="HiveCatalogue_post_save")


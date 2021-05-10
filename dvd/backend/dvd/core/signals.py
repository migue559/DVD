from django.db.models.signals import post_save, m2m_changed
from graphene_subscriptions.signals import post_save_subscription

from .models import User
print("User")
print(User)

post_save.connect(post_save_subscription, sender=User, dispatch_uid="User_post_save")

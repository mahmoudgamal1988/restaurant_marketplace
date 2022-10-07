from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from accounts.models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_user_profile(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('User Profile is created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            print('User Profile is updated')
        except:
            UserProfile.objects.create(user=instance)
            print('User Profile didn\'t exits, I have created a new one.')

# this is another way instead of using the decorator
#post_save.connect(post_save_create_user_profile, sender=User)


@receiver(pre_save, sender=User)
def pre_save_create_profile(sender, instance, **kwargs):
    print(instance.username, "is being created")

from datetime import timezone
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from warehouse.models import Product, ProductGallery


@receiver(pre_save, sender=Product)
def set_default_modified(sender, instance, **kwargs):
    instance.modified = timezone.now()


@receiver(post_save, sender=ProductGallery)
def set_default_gallery(sender, instance, **kwargs):
    if instance.is_default:
        ProductGallery.objects.filter(
            product=instance.product).exclude(id=instance.id).update(
                is_default=False)

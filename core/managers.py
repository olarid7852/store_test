from django.db.models import manager


class SoftDeleteModelManager(manager.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)

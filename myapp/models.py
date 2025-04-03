from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class AbstractBaseModel(models.Model):
    content_type = models.ForeignKey(
        ContentType, on_delete=models.SET_NULL, null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    related_object = GenericForeignKey("content_type", "object_id")
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class AbstractDerivedModel(AbstractBaseModel):
    related_object = None  # Override GenericForeignKey
    description = None

    class Meta:
        abstract = True


class ConcreteEntity(AbstractDerivedModel):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = False

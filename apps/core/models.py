from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class BaseModel(models.Model):
    cleated_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='created_%(model_name)ss')
    updated_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='updated_%(model_name)ss')

    @property
    def class_name(self):
        return self.__class__.__name__

    class Meta:
        abstract = True
        ordering = ['id']

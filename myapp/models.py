from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ValidateModelMixin(object):
    def save(self, *args, **kwargs):
        """Call :meth:`full_clean` before saving."""
        self.full_clean()
        super(ValidateModelMixin, self).save(*args, **kwargs)


class ModelBase(models.Model):
    """ Abstract class for dealing with Users and dates and othes """
    class Meta:
        abstract = True
    dt_creation = models.DateTimeField(auto_now_add=True)
    dt_modification = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)


class State(models.Model):
    code = models.CharField(max_length=6, unique=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.code + ' - ' + self.nom


class Entity(ValidateModelMixin, ModelBase):

    code = models.CharField(max_length=6, unique=True)
    nom = models.CharField(max_length=255)
    valeur = models.IntegerField(default = 0)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.code + ' - ' + self.nom + ' - val: ' + str(self.valeur)
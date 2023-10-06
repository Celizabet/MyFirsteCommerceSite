from django.db import models
from django.utils import timezone

# Create your models here.
class BasePublishModel(models.Model): 
    class PublishStateOptions(models.TextChoices):
        PUBLISHED = "PU", "PUBLICADO"
        DRAFT = "BR", "BORRADOR"
        PRIVATE = "PR", "PRIVADO"

    state = models.CharField(max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT)
    # timestamp de creación
    timestamp = models.DateTimeField(auto_now_add=True)
    # timestamp de actualización
    updated = models.DateTimeField(auto_now_add=True)
    # timestamp de publicación
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    
    class Meta:
        # Vuelve a la clase abstracta
        abstract = True
        # Al poner el menos se invierte el orden y quedan los mas recientes en actualizarse y crearse
        ordering =("-updated", "-timestamp")

    # Valida que el estado sea publicado, en caso de no tener timestamp le agrega la fecha y hora de ese momento
    #si ya tiene timestamp no agrega un nuevo ts, en caso de que el estado no sea publicado el publish_time_stamp
    #va a ser nulo
    def save(self, *args, **kwargs):
        if self.state_is_published and self.publish_timestamp in None:
            self.publish_timestamp = timezone.now()
        else: 
            self.publish_timestamp = None
        super().save(*args, **kwargs)

    # Propiedad que valida si está publicado
    @property
    def state_is_published(self):
        return self.state == self.PublishStateOptions.PUBLISHED 

    def is_published(self):
        publish_timestamp = self.publish_timestamp
        # Validar el atributo y los que se publicaron en el pasado
        return self.state_is_published and publish_timestamp < timezone.now()

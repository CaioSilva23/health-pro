from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=70, blank=False, null=False)
    celular = models.CharField(max_length=14, blank=False, null=False)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome


class AlertasCrise(models.Model):
    RATING_CHOICES = (
        ('P', 'Pânico'),
        ('A', 'Ansiedade'),
        ('D', 'Depressão'),
    )
    nota_alerta = models.CharField(max_length=1, choices=RATING_CHOICES)

    horario_acontecimento = models.DateTimeField()
    horario_superou_crise = models.DateTimeField()
    
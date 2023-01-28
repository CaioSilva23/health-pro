from django.db import models





class AvaliacaoDiaria(models.Model):
    RATING_CHOICES = (
        ('E', 'Excelente'),
        ('B', 'Bom'),
        ('R', 'Ruim'),
        ('P', 'Péssimo'),
    )
    
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)

    anotacao_positiva = models.TextField(null=True, blank=True)
    anotacao_negativa = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.rating



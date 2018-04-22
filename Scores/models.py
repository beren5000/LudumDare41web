from django.db import models

# Create your models here.

class Scores(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    modified = models.DateTimeField(auto_now=True, verbose_name="Modified")
    name = models.CharField(max_length=100,null=False, verbose_name="Player Name")
    score = models.IntegerField(default=0, verbose_name="Score")

    class Meta:
        verbose_name = "Score"
        verbose_name_plural = "Scores"


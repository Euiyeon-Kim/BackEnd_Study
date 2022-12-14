from django.db import models

# Create your models here.

class House(models.Model):
    """
        Model for house
    """
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(verbose_name="주소", max_length=140, help_text="도로명주소로 작성하시오")
    pet_allowed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
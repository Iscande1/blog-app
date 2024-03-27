from django.db import models

class Sneaker(models.Model):
    name = models.CharField("Наиминование кроссовки", max_length=100)
    description = models.TextField("Описание")
    image = models.CharField("ссылка на фото", max_length=500)
    price = models.IntegerField("Цена")

    def __str__(self):
        return self.name



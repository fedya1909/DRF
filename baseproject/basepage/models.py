from django.db import models



class User(models.Model):
    name = models.CharField("Имя пользователя", max_length=150)
    level = models.PositiveIntegerField("Уровень", default=1)
    balance = models.PositiveIntegerField("Баланс", default=0)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Имя пользователя"
        verbose_name_plural = "Имена пользователей"


class Album(models.Model):
    name = models.CharField("Имя альбома", max_length=150)
    image = models.ImageField("Фото", upload_to="album/")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Имя альбома"
        verbose_name_plural = "Имена альбомов"


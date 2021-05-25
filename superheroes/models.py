from django.db import models


class Universe(models.Model):
    name = models.CharField(max_length=100)
    date_foundation = models.DateField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'universe'


class Character(models.Model):
    universe_id = models.ForeignKey(Universe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=200)
    image2 = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'characters'


class Powers(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'powers'


class Powers_character(models.Model):
    powers_id = models.ForeignKey(Powers, on_delete=models.CASCADE)
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'powers_character'

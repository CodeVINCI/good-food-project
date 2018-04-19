from django.db import models


class Complain(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    university_name = models.CharField(max_length=200, default='')
    university_address = models.TextField(max_length=400)
    quality_choice = [(1, 'bad'), (2, 'bearable'),
                      (3, 'medium'), (4, 'good'), (5, 'select')]
    food_quality = models.IntegerField(choices=quality_choice, default=5)
    further_complain = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.email

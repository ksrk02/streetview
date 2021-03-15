from django.db import models


class Scene(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    name = models.CharField('Name', max_length=30, default='', blank=True)
    image = models.ImageField('Image', upload_to='images/')

    def __str__(self):
        return str(self.id)


class RelatedScene(models.Model):
    parent_scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    scene_id = models.IntegerField('Scene Id', default=0)
    theta = models.FloatField('Button Rotation - Y', default=0.0)

from django.db import models
from keras.preprocessing.image import load_img, img_to_array
# Create your models here.


class Image(models.Model):
    picture = models.ImageField()
    classfied = models.CharField(max_length=200, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("Image classified at {}".format(self.uploaded.strftime('%Y-%m-%d %H:%M')))

    def save(self, *args, **kwargs):

        img = load_img(self.picture, target_size=(299, 299))
        print(img)
        print('classsification failed')
        super().save(*args, **kwargs)

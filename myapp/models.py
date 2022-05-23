from django.forms import ModelForm, Textarea
from django.db import models
from django.urls import reverse

# Create your models here.

class regis(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField (max_length=100)
    password = models.CharField(max_length=100)
    confirm = models.CharField(max_length=100)



class MenPrize(models.Model):
    fullnames = models.CharField(max_length=50)
    medaltype= models.CharField(max_length=50)



class Tokyo(models.Model):
    fullname = models.CharField(max_length=55)
    sport = models.CharField(max_length=55)
    category = models.CharField(max_length=55)
    medal = models.CharField(max_length=55)



class Summer(models.Model):
    game = models.CharField(max_length=55)
    gold = models.IntegerField()
    silver = models.IntegerField()
    bronze = models.IntegerField()
    all = models.IntegerField()
    place = models.IntegerField()



class Winter(models.Model):
    game = models.CharField(max_length=55)
    gold = models.IntegerField()
    silver = models.IntegerField()
    bronze = models.IntegerField()
    all = models.IntegerField()
    place = models.IntegerField()



class Articles(models.Model):
    title = models.CharField('Name', max_length=250)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Statya')

    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новость'



class Tag(models.Model):
    page = models.CharField(max_length=20)
    title = models.CharField(max_length=20)



class Post(models.Model):
    img = models.CharField(max_length=400)
    title = models.CharField(max_length=200)
    info = models.TextField(max_length=1000)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

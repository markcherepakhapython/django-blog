from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse

class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User', 
        on_delete = models.CASCADE,
    )
    body = models.TextField()
    image = models.ImageField(blank=True, verbose_name='Изображение')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class AdditionalImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                            verbose_name='Пост')
    image = models.ImageField(verbose_name='Изображение')   


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                            verbose_name='Пост')
    author = models.CharField(max_length=30, verbose_name='Автор')
    content = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'
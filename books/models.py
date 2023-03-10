from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    google_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(verbose_name='Book Cover Image', upload_to='covers/', blank=True)
    google_cover = models.TextField(blank=True)

    def __str__(self):
        return f'{self.author}: {self.title}'

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('top', 'Top News'),
        ('tech', 'Technology'),
        ('sports', 'Sports'),
        ('entertainment', 'Entertainment'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.URLField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models


class Posts(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
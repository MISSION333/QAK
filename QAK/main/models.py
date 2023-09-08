from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250, blank=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Section(models.Model):
    title = models.CharField(max_length=250, blank=False)
    content = models.TextField()
    blog = models.ForeignKey(
            Blog,
            related_name='sections',
            on_delete=models.CASCADE
            )

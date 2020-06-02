from django.db import models


class ArticleToRead(models.Model):

    name = models.CharField(max_length=200)
    body = models.TextField(max_length=10000)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return "%s, %s, %s, %s" % (self.name, self.body, self.author, self.category)



class Category(models.Model):
    name_category = models.CharField(max_length=50)

    def __str__(self):
        return self.name_category

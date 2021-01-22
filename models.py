from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Resources(models.Model):
    title = models.CharField(max_length=300, null=True)
    links = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    category = models.ManyToManyField(Category)
    cost = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    client = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title

class Visitor(models.Model):
    name = models.CharField(max_length=300, null=True)
    resources = models.ForeignKey(Resources, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class VisitLog(models.Model):
    visitor = models.ForeignKey(Visitor, null=True, on_delete=models.SET_NULL)
    visit_freq = models.CharField(max_length=200, null=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    resource = models.ManyToManyField(Resources, null=True)


    def __str__(self):
        return str(self.visitor)

class LoginCredentials(models.Model):
    name = models.ForeignKey(Visitor, null=True, on_delete=models.SET_NULL)
    username = models.CharField(max_length=200, null=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    password = models.CharField(max_length=16, null=True)


    def __str__(self):
        return str(self.name)



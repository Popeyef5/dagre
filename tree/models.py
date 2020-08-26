from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)

class Discussion(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Statement(models.Model):
    COUNTER = 'counter'
    PREMISE = 'premise'
    SUPPORT = 'support'

    types = [(COUNTER, 'Counter'),
             (PREMISE, 'Premise'),
             (SUPPORT, 'Support')]

    discussion = models.ForeignKey(Discussion, null=True, on_delete=models.SET_NULL, related_name='statements')
    parents = models.ManyToManyField('self', related_name='responses')
    type = models.CharField(max_length=200, choices=types)
    text = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Source(models.Model):
    statements = models.ManyToManyField(Statement, related_name='sources')
    link = models.CharField(max_length=300)
    keywords = models.CharField(max_length=200, null=True)

class Reference(models.Model):
    link = models.CharField(max_length=300)
    statements = models.ManyToManyField(Statement, related_name='references')

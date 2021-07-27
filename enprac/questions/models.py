from django.db import models

# Create your models here.

class Tense(models.Model):
    ques = models.TextField()
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    answer = models.CharField(max_length=10)

    def __str__ (self):
        return self.ques


class Article(models.Model):
    ques = models.TextField()
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    answer = models.CharField(max_length=10)

    def __str__ (self):
        return self.ques


class Vocabulary(models.Model):
    ques = models.TextField()
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    answer = models.CharField(max_length=10)

    def __str__ (self):
        return self.ques


class Subject_Verb_Agreement(models.Model):
    ques = models.TextField()
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    answer = models.CharField(max_length=10)

    def __str__ (self):
        return self.ques
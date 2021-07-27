from django.contrib import admin
from questions.models import Subject_Verb_Agreement, Tense, Article, Vocabulary

# Register your models here.

admin.site.register(Tense)

admin.site.register(Article)

admin.site.register(Vocabulary)

admin.site.register(Subject_Verb_Agreement)
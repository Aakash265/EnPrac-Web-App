from django.shortcuts import render
from django.views import View
from questions.models import Subject_Verb_Agreement, Tense, Article, Vocabulary

# Create your views here.

class Question(View):
    def get(self, request):
        return render(request, 'topics/topic.html')


class TenseView(View):
    def get(self, request):
        context = { 'data': Tense.objects.all() }
        return render(request, 'topics/tense.html', context)


class ArticleView(View):
    def get(self, request):
        context = { 'data': Article.objects.all() }
        return render(request, 'topics/article.html', context)


class VocabularyView(View):
    def get(self, request):
        context = { 'data': Vocabulary.objects.all() }
        return render(request, 'topics/vocabulary.html', context)


class SubjectView(View):
    def get(self, request):
        context = { 'data': Subject_Verb_Agreement.objects.all() }
        return render(request, 'topics/subject.html', context)
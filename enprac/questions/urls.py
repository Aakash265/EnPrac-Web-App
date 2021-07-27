from django.urls import path
from questions.views import Question, TenseView, ArticleView, VocabularyView, SubjectView

urlpatterns = [
    path('topics', Question.as_view()),
    path('topics/tense', TenseView.as_view()),
    path('topics/article', ArticleView.as_view()),
    path('topics/vocabulary', VocabularyView.as_view()),
    path('topics/subject', SubjectView.as_view()),
]
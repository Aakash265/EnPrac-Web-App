from django.urls import path
from dictionary.views import SearchView, ResultView

urlpatterns = [
    path('search', SearchView.as_view()),
    path('search/mean', ResultView.as_view()),
]
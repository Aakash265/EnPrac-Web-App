from django.shortcuts import render
from django.views import View
from PyDictionary import PyDictionary

# Create your views here.

class SearchView(View):
    def get(self, request):
        return render(request, "dict/search.html")

class ResultView(View):
    def post(self, request):
        word = request.POST["value"]
        object = PyDictionary()
        meaning = object.meaning(word)
        syn = object.synonym(word)
        ant = object.antonym(word)

        # var = Dict(word=word, time=datetime.now())
        # var.save()

        return render(request, "dict/result.html", {'Word':word, 'Meaning':meaning, 'Synonym':syn, 'Antonym': ant})
import json
from django.shortcuts import render,redirect
from .wordSearch import search, sorting
from django.http import HttpResponse, JsonResponse

# Create your views here.
def homePage_view(req):
    return render(req,'wordSearchApp/homePage.html')

def wordSearch_view(req):
    return render(req, 'wordSearchApp/wordSearch.html')

def autoSuggestion_view(req):
    if req.is_ajax():
        searchWord = req.GET.get('term', '')
        results = sorting(search(searchWord.lower()), searchWord.lower())
        data = json.dumps(results)
    else:
          a = 'application/json'
    context = {'application/json': a, 'searchWord': searchWord}
    return render(req, 'wordSearchApp/notFound.html', context)

def getSearchResults(req):
    if req.method == 'GET':
        searchWord = req.GET.get('term') 
        if searchWord:
            searchResult = sorting(
                search(searchWord.lower()), searchWord.lower())
            context = {'searchWord': searchWord, 'Search_Result': searchResult}
            if len(searchResult) == 0:
                return render(req, 'wordSearchApp/notFound.html',context)
            else:
                return render(req, 'wordSearchApp/result.html',context)
        else:
            return redirect('/')

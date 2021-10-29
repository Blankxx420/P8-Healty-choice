from django.shortcuts import render
from search.search_form import Searchbar


def home(request):
    search_bar = Searchbar()
    context = {
        "searchbar": search_bar
    }
    return render(request, 'search/home.html', context)


from django.shortcuts import render
from search.search_form import Searchbar
from search.models.product import Product
from search.models.category import Categories


def home(request):
    search_bar = Searchbar()
    context = {
        "searchbar": search_bar
    }
    return render(request, 'search/home.html', context)


def products(request):
    if request.method == "POST":
        product_search = request.POST["product_search"]
        products = Product.objects.all().filter(
            name__contains=product_search.strip().lower().capitalize()
        )[:6]
        context = {
            # title in HTML will contain value of product_search
            "title": product_search,
            "products": products,
        }
        # send context to products.html template and render this template
        return render(request, "search/products.html", context)


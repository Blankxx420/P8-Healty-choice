from django.shortcuts import render
from search.search_form import Searchbar
from search.models.product import Product


def home(request):
    search_bar = Searchbar()
    context = {
        "searchbar": search_bar
    }
    return render(request, 'search/home.html', context)


def products(request):
    if request.method == "POST":
        product_search = request.POST["product_search"]
        products_obj = Product.objects.all().filter(
            name__contains=product_search.strip().lower().capitalize()
        )[:6]
        context = {
            # title in HTML will contain value of product_search
            "title": product_search,
            "products": products_obj,
        }
        # send context to products.html template and render this template
        print(context)
        return render(request, "search/products.html", context)

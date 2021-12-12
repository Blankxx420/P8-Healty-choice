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
        print(products_obj)
        context = {
            # title in HTML will contain value of product_search
            "title": product_search,
            "products": products_obj,
        }
        print(context)
        # send context to products.html template and render this template
        return render(request, "search/products.html", context)


def product(request, product_id):
    """Displays the product details page
    Args:
        product_id (int): Id of the product
    """
    # try:
    product_obj = Product.objects.get(pk=product_id)
    context = {"product": product_obj}
    # except Product.DoesNotExist:
    print(context)
    return render(request, "search/product.html", context)


def legal_notice():
    return render("search/legal_notice.html")

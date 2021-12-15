from django.db.models import Count
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
        request: base parameter
        product_id (int): Id of the product
    """
    # try:
    product_obj = Product.objects.get(pk=product_id)
    context = {"product": product_obj}
    # except Product.DoesNotExist:
    print(context)
    return render(request, "search/product.html", context)


def substitutes(request, product_id):
    """ Display substitutes from selected product"""
    # Find product searched by user with id
    product_query = Product.objects.get(pk=product_id)

    # Find the category of the product
    product_query_cat = Categories.objects.filter(product_id=product_query.id)

    # Find 9 products with better nutrition_score in the same category
    substitutes_prod = (
        Product.objects.filter(categories__in=product_query_cat)
        .annotate(nb_cat=Count("categories"))
        .filter(nb_cat__gte=3)
        .filter(nutriscore__lt=product_query.nutrition_score)
        .order_by("nutrition_score")[:9]
    )

    context = {"product": product_query, "substitutes": substitutes_prod}

    return render(request, "search/substitutes.html", context)


@login_required
def save_favorite


def legal_notice(request):
    return render(request, "search/legal_notice.html")

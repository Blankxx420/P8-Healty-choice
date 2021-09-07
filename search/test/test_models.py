from django.test import TestCase
from search.models.category import Categories
from search.models.product import Product
from search.models.substitute import Substitute


class CategoryTest(TestCase):

    def test_category_str(self):
        cat = Categories.objects.create(name="Snack")
        self.assertEqual(str(cat), "Snack")


class ProductTest(TestCase):

    def test_product_str(self):
        product = Product.objects.create(
            name="Prince",
            barcode=7622210449283,
            url="https://fr.openfoodfacts.org/produit/7622210449283/prince-lu",
            url_image="https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.415.400.jpg",
            url_image_small="https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.415.200.jpg",
            brands="Lu, Prince, Mondelez",
            nutrition_score="d",
            energy_100g=0.0,
            sugars_100g=4.8,
            sodium_100g=4.04,
            fat_100g=1.6,
            salt_100g=0.1,
        )
        self.assertEqual(str(product), "Prince" "d")
        
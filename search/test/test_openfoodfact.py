from django.test import TestCase
from search.openfoodfact import Openfoodfact
from unittest.mock import patch


class MockResponse:
    def __init__(self):
        status_code = 200

    def json(self):
        return {
            "page": 1,
            "products": [
                {
                    "product_name_fr": "Prince",
                    "code": "7622210449283",
                    "brands": "Lu, Prince, Mondelez",
                    "nutriscore_grade": "",
                    "url": "https://fr.openfoodfacts.org/produit/7622210449283/prince-lu",
                    "image_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.415.400"
                                 ".jpg",
                    "image_small_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.415."
                                       "200.jpg",
                    "categories": "Snacks, Snacks sucrés, Biscuits et gâteaux, Biscuits, Biscuits au chocolat",
                    "nutriments": {
                        "energy_100g": 0.0,
                        "sugars_100g": 4.8,
                        "sodium_100g": 4.04,
                        "fat_100g": 1.6,
                        "salt_100g": 0.1,
                    },
                },
                {
                    "product_name_fr": "Nutella",
                    "code": "3017620422003",
                    "brands": "Ferrero, Nutella",
                    "nutriscore_grade": "e",
                    "url": "https://fr.openfoodfacts.org/produit/3017620422003/nutella-ferrero",
                    "image_url": "https://static.openfoodfacts.org/images/products/301/762/042/2003/front_fr"
                                 ".248.400.jpg",
                    "image_small_url": "https://static.openfoodfacts.org/images/products/301/762/042/2003/front_fr"
                                       ".248.200.jpg",
                    "categories": "Produits à tartiner, Petit-déjeuners, Aides culinaires, Produits à tartiner sucrés,"
                                  " Aides à la pâtisserie, Pâtes à tartiner, Pâtes à tartiner aux noisettes,"
                                  " Pâtes à tartiner au chocolat, Pâtes à tartiner aux noisettes et au cacao,"
                                  " Aide culinaire sucrée",
                    "nutriments": {
                        "energy_100g": 0.0,
                        "sugars_100g": 56.3,
                        "sodium_100g": 0.0428,
                        "fat_100g": 30.9,
                        "salt_100g": 0.107,
                    },
                },
            ],
        }


mocked_product_full = {
            "product_name_fr": "Prince",
            "code": "7622210449283",
            "brands": "Lu, Prince, Mondelez",
            "nutriscore_grade": "",
            "url": "https://fr.openfoodfacts.org/produit/7622210449283/prince-lu",
            "image_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.415.400.jpg",
            "image_small_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.415.200.jpg",
            "categories": "Snacks, Snacks sucrés, Biscuits et gâteaux, Biscuits, Biscuits au chocolat",
            "nutriments": {
                "energy_100g": 0.0,
                "sugars_100g": 4.8,
                "sodium_100g": 4.04,
                "fat_100g": 1.6,
                "salt_100g": 0.1,
            },
        }


class Testopenfoodfact(TestCase):

    @patch("requests.get", return_value=MockResponse())
    def test_call_external_api(self, mocked):
        openfood = Openfoodfact()
        expected_product = MockResponse.json().get("products")
        self.assertEqual(openfood.products, expected_product)

    def test_avoid_empty(self):
        openfood = Openfoodfact()
        openfood.products = mocked_product_full
        expected_full_product = {
            "product_name_fr": "Prince",
            "code": "7622210449283",
            "brands": "Lu, Prince, Mondelez",
            "nutriscore_grade": "D",
            "url": "https://fr.openfoodfacts.org/produit/7622210449283/prince-lu",
            "image_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.415.400.jpg",
            "image_small_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.415.200.jpg",
            "categories": "Snacks, Snacks sucrés, Biscuits et gâteaux, Biscuits, Biscuits au chocolat",
            "nutriments": {
                "energy_100g": 0.0,
                "sugars_100g": 4.8,
                "sodium_100g": 4.04,
                "fat_100g": 1.6,
                "salt_100g": 0.1,
            },
        }
        self.assertEqual(openfood.avoid_empty(), expected_full_product)

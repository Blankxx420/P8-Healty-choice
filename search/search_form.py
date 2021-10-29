from django import forms


class Searchbar(forms.Form):
    product_search = forms.CharField(
        label="",
        max_length=70,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Entrez un produit",
                "class": "form-control",
                "type": "text",
                "autofocus": "autofocus",
            }
        ),
    )
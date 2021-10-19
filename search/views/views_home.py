from django.shortcuts import render


def home():
    render("templates/home.html", template_name=home)

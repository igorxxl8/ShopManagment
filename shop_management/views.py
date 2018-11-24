from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    """The home page for Learning Log."""
    return render(request, 'shop_management/index.html')


@login_required
def shops(request):
    """Show all topics."""
    return render(request, 'shop_management/shops.html')

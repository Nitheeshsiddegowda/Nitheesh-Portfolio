from django.shortcuts import render

from .data import PORTFOLIO


def index(request):
    """
    Single-page portfolio. All content comes from portfolio/data.py —
    this view just hands it to the template, it never needs editing
    when you update your info.
    """
    return render(request, 'portfolio/index.html', {"data": PORTFOLIO})

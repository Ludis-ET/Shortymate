from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from .models import ShortenedURL


def index(request):
    short = ShortenedURL
    new = old = ""
    current_site = get_current_site(request)
    if request.method == "POST":
        url = request.POST['url']
        link = short.objects.create(long_url=url)
        new = current_site.domain + "/" + link.short_code
        old = link.long_url
    return render(request, "index.html", {"new":new, "old":old})


def short(request, short):
    if ShortenedURL.objects.filter(short_code=str(short)):
        return redirect(ShortenedURL.objects.get(short_code=str(short)).long_url)
    return redirect('index')
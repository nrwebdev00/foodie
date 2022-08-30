from django.shortcuts import render


def articles(request):

  context = {}

  return render(request, 'article/article.html', context)

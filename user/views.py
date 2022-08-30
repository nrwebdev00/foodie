from django.shortcuts import render


def user(request):

  context = {}

  return render(request, 'user/user.html', context)
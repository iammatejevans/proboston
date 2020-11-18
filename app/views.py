from typing import Union

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect

from app.models import Person
from app.forms import PersonForm
from app.utils import BootstrapError


def person_form(request: WSGIRequest) -> Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]:
    """
    View to display and save Person form
    :param request: WSGI request
    :return:
    """
    if request.method == 'GET':
        form = PersonForm(error_class=BootstrapError)
        return render(request, 'homepage.html', {'form': form})
    if request.method == 'POST':
        form = PersonForm(request.POST, error_class=BootstrapError)
        if form.is_valid():
            form.save()
            return redirect('person_form')
        return render(request, 'homepage.html', {'form': form})

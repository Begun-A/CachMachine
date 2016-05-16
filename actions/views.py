from datetime import datetime

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


from models import User, Operation
from utils import split_number, check_is_active, check_auth, check_existence


def login_page(request):
    """
    View login pages, which consist with enter card number and pin.
    """
    if request.POST and request.is_ajax():
        # when enter card number
        number = request.POST.get('number', None)
        if number:
            number = int('{0}{1}{2}{3}'.format(*number.split('-')))
            card = User.objects.filter(card_number=int(number)).first()

            response = check_existence(card)
            if not response['success']:
                return JsonResponse(response)

            response = check_is_active(card)
            if not response['success']:
                return JsonResponse(response)

            response = JsonResponse(response)
            response.set_cookie('number', value=card.card_number, httponly=True)
            return response
        # when enter card pin
        pin = request.POST.get('pin', None)
        if pin:
            number = request.COOKIES.get('number')
            card = User.objects.filter(card_number=int(number)).first()

            auth = authenticate(card_number=card.card_number, password=pin)
            response = check_auth(card, auth)
            if not response['success']:
                return JsonResponse(response)

            login(request, auth)
            card.attempts = 0
            card.save()
            response = JsonResponse(
                {"success": True, "redirect": reverse('operations')})
            return response
    return render(request, 'login_page.html', {})


@login_required
def operations(request):
    """ View operations cache machine"""
    return render(request, 'operations.html', {})


@login_required
def balance(request):
    """ View card  balans and store this operation in db"""
    card = request.user
    date = datetime.utcnow()
    operation = Operation(card=card, date=date, operation='0')
    operation.save()
    content = {'date': date.date, 'balance': card.balance,
               'card': split_number(card.card_number)}
    return render(request, 'balance.html', content)


@login_required
def withdrawal(request):
    """ View withdrawal process, """
    if request.POST:
        date = datetime.utcnow()
        card = request.user
        amount = int(request.POST.get('amount'))
        if card.balance < amount:
            return render(request, 'error_page.html', {})
        operation = Operation(card=card, date=date, operation='1',
                              amount=amount)
        operation.save()
        card.balance -= amount
        card.save()
        content = {'date': date.date, 'balance': card.balance,
                   'card': split_number(card.card_number), 'amount': amount}
        return render(request, 'report.html', content)


    return render(request, 'withdrawal.html', {})


def exit(request):
    logout(request)
    return redirect(reverse('login_page'))

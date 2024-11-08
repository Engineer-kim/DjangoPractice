from codecs import replace_errors
from http.client import responses
from idlelib.rpc import response_queue

from django.urls import reverse

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound ,HttpResponseRedirect

monthly_challenges = {
    "january": "This January",
    "february": "This February",
    "march": "This March",
    "april": "This April",
    "may": "This May",
    "june": "This June",
    "july": "This July",
    "august": "This August",
    "september": "This September",
    "october": "This October",
    "november": "This November",
    "december": None,
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    # for month in months:
    #     captialized_month = month.capitalize()
    #     month_path = reverse("monthly_challenge" ,args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{captialized_month}</a></li>"

    return render(request , "challenges/index.html" ,{
        "months": months,
    })

def montly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Montly Challenge Not Found")

    redirect_month = months[month - 1]
    redirect_path = reverse("monthly_challenge" , args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request , month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request ,"challenges/challenge.html" , {
            "text": challenge_text,
            "month_name": month,
        })
    except:
        raise Http404("Monthly Challenge Not Found")


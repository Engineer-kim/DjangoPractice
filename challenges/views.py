from codecs import replace_errors
from http.client import responses

from django.urls import reverse

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound ,HttpResponseRedirect
from django.template.loader import render_to_string

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
    "december": "This December",
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        captialized_month = month.capitalize()
        month_path = reverse("monthly_challenge" ,args=[month])
        list_items += f"<li><a href=\"{month_path}\">{captialized_month}</a></li>"



    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

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
            "month_name": month.capitalize(),
        })
    except:
        return HttpResponseNotFound("<h1>This is not a valid month</h1>")

from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.shortcuts import redirect
from django.urls import reverse


# challenges/views.py
monthly_challenges = {
    'january': 'Exercise daily for 30 minutes',
    'february': 'Read one book',
    'march': 'Learn something new each day',
    'april': 'Drink at least 2 liters of water daily',
    'may': 'Wake up early every day',
    'june': 'Practice a new skill for 20 minutes daily',
    'july': 'Avoid junk food for the entire month',
    'august': 'Write a daily journal entry',
    'september': 'Learn and revise one topic each day',
    'october': 'Limit social media usage to 30 minutes per day',
    'november': 'Express gratitude by writing one thankful note daily',
    'december': None,
    # 'december': 'Reflect on the year and plan goals for next year',
}

# Create your views here.
def index(request):
    # list_items=""

    months=list(monthly_challenges.keys())
    return render(request,"testapp/index.html",{
        'months':months,
    })

    # for month in months:
    #     capital_month=month.capitalize()
    #     redirect_url=reverse('monthly-challange',args=[month.lower()])
    #     # redirect_url='/app/jan'
    #     list_items+=f"<li><a href='{redirect_url}'>{capital_month}</a></li>"

#     html="""
# <ul>
#                 <li><a href="/app/january/">January</a></li>
#                 <li><a href="/app/february/">February</a></li>
# </ul>
# """

    # return HttpResponse(f"<ul>{list_items}</ul>")



# def january(request):
#     return HttpResponse("Janauary is 1st month of the year")
# def february(request):
#     return HttpResponse("February is 2nd month of the year")
# def march(request):
#     return HttpResponse("March is 3rd month of the year")


def monthlychallange(request,month):
    try:
        challenge_text=monthly_challenges[month.lower()]
        # return HttpResponse(f"<h1>{challenge_text}</h1>")

        return render(request,"testapp/challange.html",{
            'text':challenge_text,
            'month_name':month.capitalize(),
        })
    
    except KeyError:
        # return HttpResponseNotFound("<h1>are you stupid</h1> ")
        raise Http404()



def monthlychallange_by_num(request,month):
    months=list(monthly_challenges.keys())
    redirect_month=months[month-1]



    # return HttpResponseRedirect(f"/testapp/{redirect_month}")


    # return redirect(f"/testapp/{redirect_month}")
    redirect_url=reverse("monthly-challange",args=[redirect_month])
    return redirect(redirect_url)


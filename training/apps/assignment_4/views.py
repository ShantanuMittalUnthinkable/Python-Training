from datetime import datetime
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from .my_date.date_operations import get_age_from_birth_date, get_birth_date, get_current_datetime, time_to_50

class Assignment4View(View):

    def get(self, request):
        
        return render(
            request, 
            'assignment_4/4.html'
        )

class GetCurrentDateTimeView(View):

    def get(self, request):

        return JsonResponse(
            {
                'current_datetime': str(
                    get_current_datetime()
                )
            }
        )

class BirthDateFromText(View):

    def post(self, request):

        return JsonResponse(
            {
                'birth_date' : get_birth_date(request.POST.get('age'))
            }
        )

class TextFromBirthDate(View):

    def post(self, request):

        birth_date = datetime.strptime(
            request.POST.get('birth_date'),
            "%Y-%m-%d"
        ).date()

        return JsonResponse(
            {
                'age' : get_age_from_birth_date(birth_date)
            }
        )

class TimeTo50View(View):

    def post(self, request):

        birth_date = datetime.strptime(
            request.POST.get('birth_date'),
            "%Y-%m-%d"
        ).date()

        return JsonResponse(
            {
                'age' : time_to_50(birth_date)
            }
        )
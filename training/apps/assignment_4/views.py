from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from .my_date.date_operations import get_age_from_birth_date, get_birth_date, get_current_datetime

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

    @method_decorator(csrf_exempt)
    def post(self, request):

        return JsonResponse(
            {
                'birth_date' : get_birth_date(request.POST.get('age'))
            }
        )
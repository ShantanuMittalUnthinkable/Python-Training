from django.views import View
from django.shortcuts import render

class Assignment5View(View):

    def get(self, request):
        
        context = {}

        return render(request, 'assignment_5/5.html', context=context)

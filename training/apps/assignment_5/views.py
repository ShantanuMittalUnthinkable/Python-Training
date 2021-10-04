import json

from django.http.response import JsonResponse
from django.views import View
from django.shortcuts import render

from .q3 import LinkedList
from .q2 import Car
from .q1 import Shape

class Assignment5View(View):

    def get(self, request):
        
        context = {
            'child_classes': [
                {
                    'name': shape.__name__,
                    'args': shape.get_args()
                } for shape in Shape.__subclasses__()
            ],
            'car_child_classes': [
                {
                    'name': car.__name__,
                    'args': car.get_extra_args()
                } for car in Car.__subclasses__()
            ]
        }

        return render(request, 'assignment_5/5.html', context=context)

class Q1View(View):

    def post(self, request):

        shape = Shape.get(request.POST['name'])

        shape_obj = shape(kwargs=json.loads(request.POST['kwargs']))

        return JsonResponse(
            {
                'area': shape_obj.area()
            }
        )    

class Q2View(View):

    def post(self, request):

        subclass = Car.get(request.POST['name'])
        subclass_obj = subclass(
            speed=request.POST['speed'],
            regular_price=request.POST['regular_price'],
            color=request.POST['color'],
            kwargs=request.POST
        )

        return JsonResponse(
            {
                'price': subclass_obj.doublegetSalePrice()
            }
        )

class Q3View(View):

    def post(self, request):

        linked_list = LinkedList

        ops = {
            1: ""
        }
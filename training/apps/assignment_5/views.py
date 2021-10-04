import json

from django.http.response import JsonResponse
from django.views import View
from django.shortcuts import render

from .q3 import LinkedList, Node
from .q2 import Car
from .q1 import Shape

global_ll = None

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

        global global_ll

        if not global_ll:
            global_ll = LinkedList()

        ops = {
            1: global_ll.append_node,
            2: global_ll.add_node,
            3: global_ll.delete_node,
            4: global_ll.search_node,
            6: global_ll.reverse
        }

        operation = int(request.POST.get('operation'))

        response = None

        callable = ops[operation]
        if operation != 6:
            try:
                if 'key' in request.POST.keys() and 'node' in request.POST.keys():
                    node = Node(data=request.POST.get('node'))
                    response = callable(request.POST.get('key'), node)
                elif 'node' in request.POST.keys() and not 'key' in request.POST.keys():
                    node = Node(data=request.POST.get('node'))
                    response = callable(node)
                elif 'key' in request.POST.keys() and not 'node' in request.POST.keys():
                    response = callable(request.POST.get('key'))
            except Exception as e:
                response = str(e)
        else:
            callable()

        return JsonResponse(
            {
                'response': response,
                'list': global_ll.display_all()
            }
        )
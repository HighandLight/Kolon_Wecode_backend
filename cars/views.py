import json
from json.decoder import JSONDecodeError

from django.http  import JsonResponse
from django.views import View

from cores.utils import admin_login_decorator
from cars.models import Car
from testcar.models import TestCar

class CarInformationView(View):
    @admin_login_decorator
    def get(self, request): 
        try :
            data   = json.loads(request.body)
            number = data['number']
            owner  = data['owner']
            
            if not TestCar.objects.filter(number = number, owner = owner).exists():
                return JsonResponse({'message' : 'INVALID_CAR_NUMBER_OR_OWNER'}, status=404)
            
            cars = TestCar.objects.filter(number = number, owner = owner)
            
            results = [{
                    'number':car.number,
                    'owner':car.owner,
                    'manufacturer':car.manufacturer,
                    'car_name':car.car_name,
                    'trim':car.trim,
                    'body_shape':car.body_shape,
                    'color':car.color,
                    'model_year':car.model_year,
                    'first_registration_year':car.first_registration_year,
                    'mileage':car.mileage,
                    'engine':car.engine,
                    'transmission':car.transmission,
                    'factory_price':car.factory_price,
                    'transaction_price':car.transaction_price,
                    'test_insurance_history' : [history.history for history in car.testinsurancehistory_set.all()],
                    'test_transaction_history' : [history.history for history in car.testtransactionhistory_set.all()]
            }for car in cars]
            
            return JsonResponse({"results": results}, status=200)
        
        except KeyError: 
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
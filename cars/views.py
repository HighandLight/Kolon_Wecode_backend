import json
from json.decoder import JSONDecodeError

from django.http  import JsonResponse
from django.db import transaction
from django.views import View

from cores.utils import login_decorator
from cars.models import Car, InsuranceHistory, TransactionHistory
from testcar.models import TestCar

class CarInformationView(View):
    @login_decorator
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

    @login_decorator
    def post(self, request):
        try :
            data                    = json.loads(request.body)
            user                    = request.user
            number                  = data['number']
            owner                   = data['owner']
            car_name                = data['car_name']
            trim                    = data['trim']
            body_shape              = data['body_shape']
            color                   = data['color']
            model_year              = data['model_year']
            first_registration_year = data['first_registration_year']
            engine                  = data['engine']
            transmission            = data['transmission']
            manufacturer            = data['manufacturer']
            factory_price           = data['factory_price']
            insurance_history       = data['insurance_history']
            transaction_history     = data['transaction_history']
            
            if Car.objects.filter(user = user, number = number).exists():
                return JsonResponse({'message' : 'THE_CAR_NUMBER_ALREADY_EXISTS'}, status=404)
            
            with transaction.atomic():
                car = Car.objects.create(
                    user                    = user,
                    number                  = number,
                    owner                   = owner,
                    car_name                = car_name,
                    trim                    = trim,
                    body_shape              = body_shape,
                    color                   = color,
                    model_year              = model_year,
                    first_registration_year = first_registration_year,
                    engine                  = engine,
                    transmission            = transmission,
                    manufacturer            = manufacturer,
                    factory_price           = factory_price,
                )
                for insurance_history in insurance_history:
                    InsuranceHistory.objects.create(
                        car     = car,
                        history = insurance_history,
                    )
                for transaction_history in transaction_history:
                    TransactionHistory.objects.create(
                        car     = car,
                        history = transaction_history,
                    )
                
                return JsonResponse({'Message': 'SUCCESS'}, status=200)
        
        except transaction.TransactionManagementError:
            return JsonResponse({'message': 'TransactionManagementError'}, status=400)
        
        except KeyError: 
            return JsonResponse({'Message' : 'KEY_ERROR'}, status=400)

class CarMarketPriceView(View):
    @login_decorator
    def get(self, request): 
        try :
            data     = json.loads(request.body)
            car_name = data['car_name']
            trim     = data['trim']
            
            cars = TestCar.objects.filter(car_name = car_name, trim = trim)
            
            results = [{
                'model_year': car.model_year,
                'price'     : car.transaction_price,
            }for car in cars]

            return JsonResponse({"results": results}, status=200)
        
        except KeyError: 
            return JsonResponse({'Message' : 'KEY_ERROR'}, status=400)

import json
import re
import bcrypt
import jwt

from django.http  import JsonResponse
from django.views import View
from kolon_wecode.settings  import SECRET_KEY, ALGORITHM

from dealers.models import Dealer

class SignUpView(View):
    def post(self, request): 
        try: 
            input_data      = json.loads(request.body)
            dealer_id       = input_data['id']
            PASSWORD_REGEX  = r"^(?=.{8,16}$)(?=.*[a-z])(?=.*[0-9]).*$"
            dealer_password = input_data['password']
            
            if Dealer.objects.filter(dealer_id = dealer_id).exists():
                return JsonResponse({'Message' : "THE_DEALER_ID_ALREADY_EXISTS"}, status=400)
            
            if not re.match(PASSWORD_REGEX, dealer_password):
                return JsonResponse({'Message' : 'INVALID_PASSWORD'}, status=400)
            
            hashed_password = bcrypt.hashpw(dealer_password.encode('UTF-8'), bcrypt.gensalt()).decode('UTF-8')
            
            Dealer.objects.create(
                dealer_id       = dealer_id,
                dealer_password = hashed_password,
                name            = input_data['name'],
                level           = input_data['level'],
                branch_id       = input_data['branch_id'],
            ) 
            return JsonResponse({'Message' : 'SUCCESS'}, status=201)
            
        except KeyError:
            return JsonResponse({'Message' : 'KeyError'}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body) 
            
            dealer_id       = data['id']
            dealer_password = data['password']
            
            dealer = Dealer.objects.get(dealer_id = dealer_id)
            
            if not bcrypt.checkpw(dealer_password.encode('utf-8'), dealer.dealer_password.encode('utf-8')):
                return JsonResponse({'Message': 'INVALID_PASSWORD'}, status = 401)
            
            access_token = jwt.encode({'id' : dealer.id}, SECRET_KEY, ALGORITHM)
            
            return JsonResponse({
                'Message'      : 'SUCCESS',
                'Access_token' : access_token
            }, status=200)
            
        except KeyError: 
            return JsonResponse({'Message': 'KeyError'}, status = 400)
        
        except Dealer.DoesNotExist:
            return JsonResponse({'Message': 'INVALID_ID'}, status = 404)

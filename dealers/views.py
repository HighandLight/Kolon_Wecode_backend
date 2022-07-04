import json
import re
import bcrypt

from django.http  import JsonResponse
from django.views import View

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
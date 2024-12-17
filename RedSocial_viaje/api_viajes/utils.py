from functools import wraps
from django.http import JsonResponse
from .models import Token

def token_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        token_key = request.headers.get('Authorization')
        if not token_key:
            return JsonResponse({'error': 'Token no proporcionado'}, status=403)
        try:
            token = Token.objects.get(key=token_key.replace('Token ', ''))
            request.user = token.user
        except Token.DoesNotExist:
            return JsonResponse({'error': 'Token inválido'}, status=403)
        return view_func(request, *args, **kwargs)
    return wrapper

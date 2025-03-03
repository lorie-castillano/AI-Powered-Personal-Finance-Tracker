from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CustomUser


@api_view(['POST'])
def register(request):
    user = CustomUser.objects.create_user(username=request.data['username'], password=request.data['password'], email=request.data['email'])
    token = RefreshToken.for_user(user)
    return Response({'refresh': str(token), 'access': str(token.access_token)})

from rest_framework import generics, parsers
from .serializers import SignUpSerializers
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class SignUp(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = SignUpSerializers
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]





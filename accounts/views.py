from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializer import SignupSerializer, SuggestionUserSerializer


# Create your views here.
class SignupView(CreateAPIView):
    model = get_user_model()
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny
    ]


class SuggestionList(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = SuggestionUserSerializer

from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, permissions

# Create your views here.

from .models import Entity

def index(request):

    return render(request, 'myapp/index.html', {'entities': Entity.objects.all()})

def vue(request):
    return render(request, 'myapp/vue.html', {})



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

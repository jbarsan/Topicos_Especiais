"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from .models import GameCategory
from .models import Game
from .models import Player
from .models import Score
from .serializers import GameCategorySerializer
from .serializers import GameSerializer
from .serializers import PlayerSerializer
from .serializers import ScoreSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


class GameCategoryList(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'

class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'

class GameList(generics.ListCreateAPIView):
    pass

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    pass

class PlayerList(generics.ListCreateAPIView):
    pass

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    pass

class ScoreList(generics.ListCreateAPIView):
    pass

class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    pass

class ApiRoot(generics.GenericAPIView):
    pass
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


from ..repositories.dog_repository import DogRepository
from ..serializers import dog_serializer
from ..model.dog import Dog

def get_all(request):
  repository = DogRepository()
  dogs = repository.get_all()
  response = dog_serializer.serialize_list(dogs)
  return JsonResponse(response, safe=False)

def get_by_id(request, id):
  repository = DogRepository()
  dog = repository.get_by_id(id)
  response = dog_serializer.serialize(dog)
  return JsonResponse(response, safe=False)

@csrf_exempt
def add(request):
  body = json.loads(request.body)
  name = body["name"]
  age = body["age"]
  dog = DogRepository().add(Dog(None, name, age))
  response = dog_serializer.serialize(dog)
  return JsonResponse(response, safe=False)

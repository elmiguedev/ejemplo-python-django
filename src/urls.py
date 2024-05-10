from django.urls import path
from django.views.decorators.http import require_POST, require_GET
from .controllers import dog_controller

urlpatterns = [
  path("dogs/", require_GET(dog_controller.get_all)),
  path("dogs/<int:id>/", require_GET(dog_controller.get_by_id)),
  path("dogs/add/", require_POST(dog_controller.add))
]
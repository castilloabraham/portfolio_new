from django.urls import path, include
from rest_framework import routers
from projects import views 

#"api/v1" -> api versioning


router = routers.DefaultRouter()
router.register(r'projects', views.ProjectView, 'projects')


#definimos los url de las rutas
urlpatterns = [
    path("api/v1", include(router.urls))
]



#Con esto generamos por defecto las rutas GET POST PUT y DELETE
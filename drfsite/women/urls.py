from django.urls import path


# from .views import (WomenViewSet)
from .views import (
    WomenAPIList,
    WomenAPIUpdate,
    WomenAPIDestroy,
)


# router = MyCastomRouter()
# router.register(r'women', WomenViewSet, basename='women')


urlpatterns = [
    # path('', include(router.urls))
    path("women/", WomenAPIList.as_view()),
    path("women/<int:pk>/", WomenAPIUpdate.as_view()),
    path("womendelete/<int:pk>/", WomenAPIDestroy.as_view()),
]

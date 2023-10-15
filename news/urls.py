from django.urls import include, path
from .views import AllArticleViewSet, docs_view, dev_view
from rest_framework import routers



app_name = "news"

router = routers.DefaultRouter()
router.register(r'', AllArticleViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    path('api/', include(router.urls)),
    path('', docs_view, name="docs"),
    path('about-me/', dev_view, name="dev_view"),
]


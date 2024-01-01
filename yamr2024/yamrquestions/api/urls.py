from django.urls import path, include
from rest_framework.routers import DefaultRouter

from yamrquestions.api import views as yqv

router = DefaultRouter()
router.register(r'questions', yqv.YamrQuestionViewSet)
# The r before the string in r'questions' is a flag indicating that the string is a raw string in Python.

urlpatterns = [
    path("", include(router.urls)),

    path("questions/<slug:slug>/answers/",
            yqv.YamrAnswerListAPIView.as_view(), name="answer-list"),

    path("questions/<slug:slug>/answer/",
         yqv.YamrAnswerCreateAPIView.as_view(), name="answer-create"),

    path("answers/<uuid:uuid>/",
            yqv.YamrAnswerRUDAPIView.as_view(), name="answer-detail"),

]
from django.contrib import admin
from yamrquestions.models import YamrQuestion, YamrAnswer

# Register your models here.
admin.site.register(YamrQuestion)
admin.site.register(YamrAnswer)

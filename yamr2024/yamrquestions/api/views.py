from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from yamrquestions.models import YamrQuestion, YamrAnswer
from yamrquestions.api.serializers import YamrQuestionSerializer, YamrAnswerSerializer
from yamrquestions.api.permissions import IsAuthorOrReadOnly

class YamrQuestionViewSet(viewsets.ModelViewSet):
    queryset = YamrQuestion.objects.all().order_by('-created_at')
    serializer_class = YamrQuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class YamrAnswerCreateAPIView(generics.CreateAPIView):
    queryset = YamrAnswer.objects.all()
    serializer_class = YamrAnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        yamrquestion_slug = self.kwargs.get("slug")
        yamrquestion = get_object_or_404(YamrQuestion, slug=yamrquestion_slug)

        if yamrquestion.yamr_answers.filter(author=request_user).exists():
            raise ValidationError("You have already answered this question!")

        serializer.save(author=self.request.user, yamrquestion=yamrquestion)

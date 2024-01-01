from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from yamrquestions.models import YamrQuestion
from yamrquestions.api.serializers import YamrQuestionSerializer
from yamrquestions.api.permissions import IsAuthorOrReadOnly

class YamrQuestionViewSet(viewsets.ModelViewSet):
    queryset = YamrQuestion.objects.all().order_by('-created_at')
    serializer_class = YamrQuestionSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
from rest_framework import viewsets, generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

from yamrquestions.models import YamrQuestion, YamrAnswer
from yamrquestions.api.serializers import YamrQuestionSerializer, YamrAnswerSerializer
from yamrquestions.api.permissions import IsAuthorOrReadOnly

class YamrQuestionViewSet(viewsets.ModelViewSet):
    queryset = YamrQuestion.objects.all().order_by('-created_at')
    serializer_class = YamrQuestionSerializer
    # permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
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

#  Provide *RUD functionality for an answer instance to it's author.
class YamrAnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView): # RUD = Retrieve Update Destroy

    queryset = YamrAnswer.objects.all()
    serializer_class = YamrAnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = 'uuid'

    # def delete(self, request, *args, **kwargs):
    #     yamranswer = YamrAnswer.objects.filter(pk=self.kwargs["pk"],
    #                                         author=request.user)
    #     if yamranswer.exists():
    #         return self.destroy(request, *args, **kwargs)
    #     else:
    #         raise ValidationError("You can not delete this answer!"

class YamrAnswerListAPIView(generics.ListAPIView):
    serializer_class = YamrAnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        yamrquestion_slug = self.kwargs.get("slug")
        return YamrAnswer.objects.filter(yamrquestion__slug=yamrquestion_slug).order_by("-created_at")
        # - on created_at means descending order (the latest answer will be on top)
        # double underscore __ means "look inside" (look inside yamrquestion for slug)
    
class AnswerLikeAPIView(APIView):
    """
    Allow users to add/remove a like to/from an answer instance.
    """

    serializer_class = YamrAnswerSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "uuid"

    def delete(self, request, uuid):
        answer = get_object_or_404(YamrAnswer, uuid=uuid)
        user = request.user

        answer.voters.remove(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(
            answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, uuid):
        """Add request.user to the voters queryset of an answer instance."""
        answer = get_object_or_404(YamrAnswer, uuid=uuid)
        user = request.user

        answer.voters.add(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
from rest_framework import serializers
from yamrquestions.models import YamrQuestion, YamrAnswer

class YamrQuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    yamr_answers_count = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    user_has_answered = serializers.SerializerMethodField()
    
    class Meta:
        model = YamrQuestion
        exclude = ['id', 'updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d, %Y')
    
    def get_yamr_answers_count(self, instance):
        return instance.yamr_answers.count()
    
    def get_user_has_answered(self, instance):
        request = self.context.get('request')
        return instance.yamr_answers.filter(author=request.user).exists()
    
class YamrAnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_liked_answer = serializers.SerializerMethodField()
    yamrquestion_slug = serializers.SerializerMethodField()
    
    class Meta:
        model = YamrAnswer
        exclude = ['id', 'updated_at', 'yamrquestion', 'voters']
    
    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d, %Y')
    
    def get_likes_count(self, instance):
        return instance.voters.count()
    
    def get_user_has_liked_answer(self, instance):
        request = self.context.get('request')
        return instance.voters.filter(pk=request.user.pk).exists()
    
    def get_yamrquestion_slug(self, instance):
        return instance.yamrquestion.slug
        
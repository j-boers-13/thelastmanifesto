from rest_framework import serializers
from .models import Article

# A serializer can turn model instances and querysets into JSON
# Nice for API with React!

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('pk','headline','trailtext','thumbnail','url','date','source')

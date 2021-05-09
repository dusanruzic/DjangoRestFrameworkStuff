from rest_framework import serializers
from blog.models import Post

#serilizer takes in memory Django object (QuerySet for example) and make python object from them, which can be easier translated into JSON format.
#Same for the vice versa, from frontend is comming JSON, which is parsed to python dict, which will be serialized to objects which is suitable to be saved in DB.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
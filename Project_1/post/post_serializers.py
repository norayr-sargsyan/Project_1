from rest_framework import serializers
from post.models import Post, Comment, Likes
from users.user_serializers import UserSerializers


class PostSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = data.pop("user")
        data["user"] = UserSerializers(user).data

        return data


class CommentSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = data.pop("user")
        data["user"] = UserSerializers(user).data

        return data


class LikeSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Likes
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = data.pop("user")
        data["user"] = UserSerializers(user).data

        return data

from rest_framework import serializers, validators

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post')


class FollowSerializer(serializers.ModelSerializer):
    curr_user = serializers.CurrentUserDefault()
    user = serializers.SlugRelatedField(slug_field='username', read_only=True,
                                        default=curr_user)
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = (validators.UniqueTogetherValidator(
            queryset=Follow.objects.all(), fields=('user', 'following')),)

    def validate_following(self, following):
        if following == self.context['request'].user:
            raise serializers.ValidationError(
                'Невозможно подписаться на самого себя')
        return following

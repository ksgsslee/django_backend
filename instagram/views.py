from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [AllowAny]

    def get_queryset(self):
        # timesince = timezone.now() - timedelta(days=3)
        qs = super().get_queryset()
        qs = qs.filter(
            Q(author=self.request.user)
            | Q(author__in=self.request.user.following_set.all())
        )
        # qs = qs.filter(created_at__gte=timesince)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)

    @action(detail=True, methods=["POST"])
    def like(self, request, pk):
        post = self.get_object()
        post.like_user_set.add(self.request.user)
        return Response(status.HTTP_201_CREATED)

    @like.mapping.delete
    def unlike(self, request, pk):
        post = self.get_object()
        post.like_user_set.remove(self.request.user)
        return Response(status.HTTP_204_NO_CONTENT)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

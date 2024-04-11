class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    
    def __str__(self):
        return self.user.username

class ProfileSerializer(serializers.ModelSerializer):
    user = UserNameSerializer(read_only=True)
    skills = SkillNameSerializer(many=True, read_only=True)
    reviews = ReviewTextSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'location', 'birth_date', 'skills', 'reviews']
        read_only_fields = ['user']

class ProfileDetailView(mixins.UpdateModelMixin, 
                        mixins.RetrieveModelMixin, 
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
         serializer.save(user=self.request.user)

def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    
Нужно переопределить def update так чтобы в поле 'skills' он принимал в себя не переопределенный skills = SkillNameSerializer(many=True, read_only=True), а skills = models.ManyToManyField(Skill, blank=True) из модели Skill 
    

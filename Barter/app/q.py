class ProfileDetailView(mixins.UpdateModelMixin, 
                        mixins.RetrieveModelMixin, 
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        user_profile = self.request.user.profile
        if user_profile:
            return user_profile
        else:
            # Если профиль пользователя не существует, создаем его
            Profile.objects.create(user=self.request.user)
            # И повторно пытаемся получить объект профиля
            return self.request.user.profile
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
нужно чтобы редактировать профиль могли только его владельцы
from rest_framework import permissions

class SkillPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_superuser
        else:
            return False
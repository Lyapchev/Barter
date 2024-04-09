from rest_framework import permissions

class SkillPermissions(permissions.BasePermission):
    """
    Пользовательские разрешения для навыков.
    """

    def has_permission(self, request, view):
        """
        Проверяет разрешения на доступ к списку навыков.
        """
        if request.method in permissions.SAFE_METHODS:
            # Разрешить все методы GET, HEAD, OPTIONS
            return True
        else:
            # Разрешить только аутентифицированным пользователям
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Проверяет разрешения на доступ к конкретному навыку.
        """
        if request.method in permissions.SAFE_METHODS:
            # Разрешить все методы GET, HEAD, OPTIONS
            return True
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            # Разрешить только суперюзерам редактировать или удалять
            return request.user.is_superuser
        else:
            # Для остальных методов возвращаем False
            return False

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit and watch it."""

    def has_object_permission(self, request, view, obj):

        # Allow GET, HEAD or OPTIONS requests for task owner.
        if request.method in permissions.SAFE_METHODS:
            if obj.owner == request.user:
                return True

        # Write permissions are only allowed to the owner of the object.
        if obj.owner == request.user:
            return obj.owner == request.user


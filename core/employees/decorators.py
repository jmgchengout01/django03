from django.contrib.auth.decorators import user_passes_test


def multiple_permissions_required(permissions):
    def check_perms(user):
        return all(user.has_perm(perm) for perm in permissions)
    return user_passes_test(check_perms)

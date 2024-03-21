from rest_framework.throttling import UserRateThrottle

class APIKeyRateThrottle(UserRateThrottle):
    scope = 'api_key'

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            return f'{self.cache_format}%s' % request.user.apikey.key
        return None
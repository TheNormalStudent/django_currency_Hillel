from rest_framework.throttling import AnonRateThrottle

class AnonUserRateThrottle(AnonRateThrottle):
    scope = 'rates_anon_trottle'
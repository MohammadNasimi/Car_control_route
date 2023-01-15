from drf_yasg import openapi

search_key = openapi.Parameter('search_key',
                              openapi.IN_QUERY, description="search_key param", type=openapi.TYPE_STRING)

date_from = openapi.Parameter('date_from',
                              openapi.IN_QUERY, description="date_from param", type=openapi.TYPE_STRING)

date_to = openapi.Parameter('date_to',
                              openapi.IN_QUERY, description="date_to param", type=openapi.TYPE_STRING)
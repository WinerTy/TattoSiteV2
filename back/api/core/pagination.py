from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BaseResultsSetPagination(PageNumberPagination):
    """
    Custom pagination class for base result sets
    """

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100
    total_pages = None

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )


class LargeResultsSetPagination(BaseResultsSetPagination):
    """

    Custom pagination class for large result sets
    """

    page_size = 1000
    page_size_query_param = "page_size"
    max_page_size = 10000


class StandardResultsSetPagination(BaseResultsSetPagination):
    """
    Custom pagination class for standard result sets
    """

    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000


class SmallResultsSetPagination(BaseResultsSetPagination):
    """
    Custom pagination class for small result sets
    """

    page_size = 9
    page_size_query_param = "page_size"
    max_page_size = 27

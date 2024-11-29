from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    """

    Custom pagination class for large result sets
    """

    page_size = 1000
    page_size_query_param = "page_size"
    max_page_size = 10000


class StandardResultsSetPagination(PageNumberPagination):
    """
    Custom pagination class for standard result sets
    """

    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000

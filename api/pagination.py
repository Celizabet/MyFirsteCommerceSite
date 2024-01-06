from rest_framework.pagination import PageNumberPagination

class ProductModelPagination(PageNumberPagination):
    page_size = 2
    page_query_param = "p" 
    last_page_strings = "end" 


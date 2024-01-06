from rest_framework.pagination import(
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination
)

class ProductModelPagination(PageNumberPagination):
    page_size = 3
    page_query_param = "p" #page
    #page_size_query_param = "size" #parámetro dinámico
    #max_page_size = 5
    last_page_strings = "end" #renombra a la última página de la lsita de productos

class ProductModelOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 3
    limit_query_param = "records" #renombra el fin de la paginación
    offset_query_param = "start" #renombra el inicio de la paginación

class ProductModelCursorPagination(CursorPagination):
    page_size = 4
    cursor_query_param = "c" #renombra el cursor
    ordering = "title"
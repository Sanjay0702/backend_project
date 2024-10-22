def get_document(queryset, filter = {}):
    obj = queryset(**filter)
    if len(obj):
        return obj[0]
    return None
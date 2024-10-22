def update_documents(queryset, filter={}, json={}):
    data = queryset(**filter).update(**json)
    return bool(data)
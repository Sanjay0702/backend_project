def save_documents(queryset, json = {}):
    obj = queryset(**json)
    obj.save()
    return obj